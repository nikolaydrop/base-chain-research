"""Compare the cost of a simple ETH transfer (21,000 gas) on Base and Ethereum L1.

Usage: python scripts/compare_fees.py [--json]
  --json  print the result as JSON instead of text

Read-only, no wallet required. Note: on Base this covers only the L2 execution
fee; the small L1 data fee is not included, so the Base number is a lower bound.
"""
import argparse
import json
import os

from web3 import Web3

from rpc import DEFAULT_RPC, connect, with_retry

BASE_RPC = os.getenv("BASE_RPC_URL", DEFAULT_RPC)
ETH_RPC = os.getenv("ETH_RPC_URL", "https://ethereum-rpc.publicnode.com")
TRANSFER_GAS = 21_000


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Compare transfer fees on Base and Ethereum L1")
    parser.add_argument("--json", action="store_true",
                        help="print the result as JSON instead of text")
    return parser.parse_args(argv)


def snapshot(w3):
    """Read the latest block and gas price and work out a transfer's cost."""
    block = with_retry(w3.eth.get_block, "latest")
    gas_price = with_retry(lambda: w3.eth.gas_price)
    return {
        "chain_id": w3.eth.chain_id,
        "block": block["number"],
        "base_fee_gwei": Web3.from_wei(block.get("baseFeePerGas", 0), "gwei"),
        "gas_price_gwei": Web3.from_wei(gas_price, "gwei"),
        "cost_eth": Web3.from_wei(gas_price * TRANSFER_GAS, "ether"),
    }


def cost_ratio(base, eth):
    """How many times more expensive Ethereum is than Base (None if Base is free)."""
    if base["cost_eth"] <= 0:
        return None
    return eth["cost_eth"] / base["cost_eth"]


def snapshot_to_dict(s):
    """Turn a snapshot into plain numbers that JSON can store."""
    return {
        "chain_id": s["chain_id"],
        "block": s["block"],
        "base_fee_gwei": float(s["base_fee_gwei"]),
        "gas_price_gwei": float(s["gas_price_gwei"]),
        "transfer_cost_eth": float(s["cost_eth"]),
    }


def result_to_dict(base, eth):
    """Both snapshots plus the cost ratio, ready for JSON."""
    ratio = cost_ratio(base, eth)
    return {
        "base": snapshot_to_dict(base),
        "ethereum": snapshot_to_dict(eth),
        "ethereum_to_base_cost_ratio": None if ratio is None else round(float(ratio), 1),
    }


def show(name, s):
    print(f"{name} (chain {s['chain_id']}, block {s['block']})")
    print(f"  Base fee:            {s['base_fee_gwei']:.6f} gwei")
    print(f"  Gas price:           {s['gas_price_gwei']:.6f} gwei")
    print(f"  Simple transfer:     {s['cost_eth']:.10f} ETH")


def main():
    args = parse_args()
    base = snapshot(connect(BASE_RPC))
    eth = snapshot(connect(ETH_RPC))

    if args.json:
        print(json.dumps(result_to_dict(base, eth), indent=2))
        return

    show("Base", base)
    print()
    show("Ethereum L1", eth)
    print()
    ratio = cost_ratio(base, eth)
    if ratio is not None:
        print(f"Ethereum L1 is about {ratio:,.0f}x more expensive than Base right now.")


if __name__ == "__main__":
    main()