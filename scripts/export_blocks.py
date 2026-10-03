"""Export basic stats for the last N Base blocks to a CSV file.

Usage: python scripts/export_blocks.py [N] [output_path]
Defaults: N=100, output_path=data/blocks.csv. Read-only, no wallet required.
"""
import csv
import os
import sys

from rpc import connect, with_retry

FIELDS = ["block", "timestamp", "tx_count", "gas_used", "gas_limit", "base_fee_wei"]


def block_row(block):
    """Turn a block into one CSV row."""
    return [
        block["number"],
        block["timestamp"],
        len(block["transactions"]),
        block["gasUsed"],
        block["gasLimit"],
        block.get("baseFeePerGas", 0),
    ]


def write_csv(path, rows):
    """Write rows with a header to path, creating folders if needed."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(FIELDS)
        writer.writerows(rows)


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    out = sys.argv[2] if len(sys.argv) > 2 else "data/blocks.csv"
    if n < 1:
        raise SystemExit("N must be at least 1")

    w3 = connect()
    latest = w3.eth.block_number
    rows = [
        block_row(with_retry(w3.eth.get_block, number))
        for number in range(latest - n + 1, latest + 1)
    ]
    write_csv(out, rows)
    print(f"Wrote {n} blocks (up to block {latest}) to {out}")


if __name__ == "__main__":
    main()