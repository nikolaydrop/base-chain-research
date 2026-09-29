"""Export basic stats for the last N Base blocks to a CSV file.

Usage: python scripts/export_blocks.py [N] [output_path]
Defaults: N=100, output_path=data/blocks.csv. Read-only, no wallet required.
"""
import csv
import os
import sys

from web3 import Web3

RPC_URL = os.getenv("BASE_RPC_URL", "https://mainnet.base.org")
FIELDS = ["block", "timestamp", "tx_count", "gas_used", "gas_limit", "base_fee_wei"]


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    out = sys.argv[2] if len(sys.argv) > 2 else "data/blocks.csv"

    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        raise SystemExit(f"Could not connect to {RPC_URL}")

    latest = w3.eth.block_number
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)

    with open(out, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(FIELDS)
        for number in range(latest - n + 1, latest + 1):
            b = w3.eth.get_block(number)
            writer.writerow([
                b["number"],
                b["timestamp"],
                len(b["transactions"]),
                b["gasUsed"],
                b["gasLimit"],
                b.get("baseFeePerGas", 0),
            ])

    print(f"Wrote {n} blocks (up to block {latest}) to {out}")


if __name__ == "__main__":
    main()
