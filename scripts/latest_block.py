"""Fetch the latest Base block. Read-only, no wallet required."""
import os
from datetime import datetime, timezone

from web3 import Web3

RPC_URL = os.getenv("BASE_RPC_URL", "https://mainnet.base.org")


def main():
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        raise SystemExit(f"Could not connect to {RPC_URL}")

    block = w3.eth.get_block("latest")
    ts = datetime.fromtimestamp(block["timestamp"], tz=timezone.utc)
    base_fee_gwei = Web3.from_wei(block.get("baseFeePerGas", 0), "gwei")

    print(f"Chain ID:     {w3.eth.chain_id}")
    print(f"Block:        {block['number']}")
    print(f"Time (UTC):   {ts}")
    print(f"Transactions: {len(block['transactions'])}")
    print(f"Gas used:     {block['gasUsed']:,} / {block['gasLimit']:,}")
    print(f"Base fee:     {base_fee_gwei:.6f} gwei")


if __name__ == "__main__":
    main()
