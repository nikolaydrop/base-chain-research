"""Compare the cost of a simple ETH transfer (21,000 gas) on Base and Ethereum L1.

Read-only, no wallet required. Note: on Base this covers only the L2 execution
fee; the small L1 data fee is not included, so the Base number is a lower bound.
"""
import os

from web3 import Web3

BASE_RPC = os.getenv("BASE_RPC_URL", "https://mainnet.base.org")
ETH_RPC = os.getenv("ETH_RPC_URL", "https://ethereum-rpc.publicnode.com")
TRANSFER_GAS = 21_000


def connect(url):
    w3 = Web3(Web3.HTTPProvider(url))
    if not w3.is_connected():
        raise SystemExit(f"Could not connect to {url}")
    return w3


def snapshot(w3):
    block = w3.eth.get_block("latest")
    gas_price = w3.eth.gas_price
    return {
        "chain_id": w3.eth.chain_id,
        "block": block["number"],
        "base_fee_gwei": Web3.from_wei(block.get("baseFeePerGas", 0), "gwei"),
        "gas_price_gwei": Web3.from_wei(gas_price, "gwei"),
        "cost_eth": Web3.from_wei(gas_price * TRANSFER_GAS, "ether"),
    }


def show(name, s):
    print(f"{name} (chain {s['chain_id']}, block {s['block']})")
    print(f"  Base fee:            {s['base_fee_gwei']:.6f} gwei")
    print(f"  Gas price:           {s['gas_price_gwei']:.6f} gwei")
    print(f"  Simple transfer:     {s['cost_eth']:.10f} ETH")


def main():
    base = snapshot(connect(BASE_RPC))
    eth = snapshot(connect(ETH_RPC))

    show("Base", base)
    print()
    show("Ethereum L1", eth)
    print()
    if base["cost_eth"] > 0:
        ratio = eth["cost_eth"] / base["cost_eth"]
        print(f"Ethereum L1 is about {ratio:,.0f}x more expensive than Base right now.")


if __name__ == "__main__":
    main()
