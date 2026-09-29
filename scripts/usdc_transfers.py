"""Show recent USDC Transfer events on Base. Read-only, no wallet required."""
import os
import sys

from web3 import Web3

RPC_URL = os.getenv("BASE_RPC_URL", "https://mainnet.base.org")
USDC = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"  # native USDC on Base
TRANSFER_TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
DECIMALS = 6


def short(addr_bytes):
    addr = Web3.to_checksum_address(bytes(addr_bytes)[-20:])
    return f"{addr[:6]}...{addr[-4:]}"


def main():
    n_blocks = int(sys.argv[1]) if len(sys.argv) > 1 else 10
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        raise SystemExit(f"Could not connect to {RPC_URL}")

    latest = w3.eth.block_number
    logs = w3.eth.get_logs({
        "fromBlock": latest - n_blocks + 1,
        "toBlock": latest,
        "address": Web3.to_checksum_address(USDC),
        "topics": [TRANSFER_TOPIC],
    })

    total = 0
    for log in logs[:15]:
        amount = int.from_bytes(bytes(log["data"]), "big") / 10**DECIMALS
        print(f"block {log['blockNumber']}: {short(log['topics'][1])} -> "
              f"{short(log['topics'][2])}  {amount:,.2f} USDC")
    for log in logs:
        total += int.from_bytes(bytes(log["data"]), "big") / 10**DECIMALS

    print(f"\nBlocks scanned:   {n_blocks}")
    print(f"USDC transfers:   {len(logs)}")
    print(f"Total moved:      {total:,.2f} USDC")


if __name__ == "__main__":
    main()
