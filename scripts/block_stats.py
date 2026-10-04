"""Print summary statistics for a blocks CSV made by export_blocks.py.

Usage: python scripts/block_stats.py [csv_path]
Default: data/blocks.csv
"""
import csv
import math
import statistics
import sys


def load_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def percentile(values, pct):
    """Nearest-rank percentile (pct from 0 to 100) of a list of numbers."""
    if not values:
        raise ValueError("values must not be empty")
    ordered = sorted(values)
    rank = max(1, math.ceil(pct / 100 * len(ordered)))
    return ordered[rank - 1]


def summarize(rows):
    """Return a dict of summary numbers for a list of CSV rows."""
    if len(rows) < 2:
        raise ValueError("need at least 2 blocks")

    tx = [int(r["tx_count"]) for r in rows]
    ts = [int(r["timestamp"]) for r in rows]
    util = [int(r["gas_used"]) / int(r["gas_limit"]) for r in rows]
    span = ts[-1] - ts[0]

    return {
        "blocks": len(rows),
        "first_block": int(rows[0]["block"]),
        "last_block": int(rows[-1]["block"]),
        "avg_interval_s": span / (len(rows) - 1),
        "tx_total": sum(tx),
        "tx_avg": sum(tx) / len(tx),
        "tx_min": min(tx),
        "tx_max": max(tx),
        "tx_median": statistics.median(tx),
        "tx_p90": percentile(tx, 90),
        "tx_p99": percentile(tx, 99),
        "tps": sum(tx) / span if span else 0.0,
        "gas_util_avg_pct": 100 * sum(util) / len(util),
        "gas_util_max_pct": 100 * max(util),
    }


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data/blocks.csv"
    s = summarize(load_rows(path))
    print(f"Blocks:            {s['blocks']} ({s['first_block']} to {s['last_block']})")
    print(f"Block interval:    {s['avg_interval_s']:.2f} s")
    print(f"Transactions:      {s['tx_total']:,} total, {s['tx_avg']:.0f} per block "
          f"(min {s['tx_min']}, max {s['tx_max']})")
    print(f"Per block:         median {s['tx_median']:.0f}, "
          f"p90 {s['tx_p90']}, p99 {s['tx_p99']}")
    print(f"Throughput:        about {s['tps']:.0f} tx/s")
    print(f"Gas utilization:   {s['gas_util_avg_pct']:.1f}% average, {s['gas_util_max_pct']:.1f}% max")


if __name__ == "__main__":
    main()