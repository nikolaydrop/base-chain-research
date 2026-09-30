"""Plot transactions per block and gas utilization from data/blocks.csv.

Usage: python scripts/plot_blocks.py [csv_path] [output_png]
Defaults: data/blocks.csv -> analysis/blocks.png
"""
import csv
import os
import sys

import matplotlib

matplotlib.use("Agg")  # no display needed
import matplotlib.pyplot as plt


def load(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def main():
    src = sys.argv[1] if len(sys.argv) > 1 else "data/blocks.csv"
    out = sys.argv[2] if len(sys.argv) > 2 else "analysis/blocks.png"

    rows = load(src)
    if not rows:
        raise SystemExit(f"No data in {src}")

    blocks = [int(r["block"]) for r in rows]
    tx = [int(r["tx_count"]) for r in rows]
    util = [100 * int(r["gas_used"]) / int(r["gas_limit"]) for r in rows]

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(9, 6), sharex=True)
    ax1.plot(blocks, tx)
    ax1.set_ylabel("Transactions per block")
    ax1.set_title(f"Base blocks {blocks[0]} to {blocks[-1]}")
    ax2.plot(blocks, util, color="tab:orange")
    ax2.set_ylabel("Gas used (% of limit)")
    ax2.set_xlabel("Block number")
    ax2.ticklabel_format(axis="x", useOffset=False, style="plain")
    fig.tight_layout()

    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    fig.savefig(out, dpi=120)
    print(f"Saved chart to {out}")


if __name__ == "__main__":
    main()
