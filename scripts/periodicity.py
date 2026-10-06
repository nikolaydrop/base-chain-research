"""Look for a repeating pattern in transactions per block.

Averages the transaction count by position inside a cycle, using the block
timestamp modulo the cycle length in seconds.

Usage: python scripts/periodicity.py [csv_path] [period_seconds]
Defaults: data/blocks.csv, 30
"""
import csv
import sys
from collections import defaultdict


def load_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


def phase_profile(rows, period):
    """Mean transactions per block for each value of timestamp % period."""
    groups = defaultdict(list)
    for r in rows:
        groups[int(r["timestamp"]) % period].append(int(r["tx_count"]))
    return {phase: sum(v) / len(v) for phase, v in sorted(groups.items())}


def peak_summary(profile):
    """Peak phase, its mean, the mean of the other phases and their ratio."""
    if len(profile) < 2:
        raise ValueError("need at least 2 phases")
    peak = max(profile, key=profile.get)
    others = [v for k, v in profile.items() if k != peak]
    rest = sum(others) / len(others)
    return {
        "phase": peak,
        "peak_mean": profile[peak],
        "other_mean": rest,
        "ratio": profile[peak] / rest if rest else 0.0,
    }


def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "data/blocks.csv"
    period = int(sys.argv[2]) if len(sys.argv) > 2 else 30
    if period < 2:
        raise SystemExit("period_seconds must be at least 2")

    rows = load_rows(path)
    profile = phase_profile(rows, period)
    s = peak_summary(profile)

    print(f"Cycle length: {period} s, blocks: {len(rows)}")
    print("phase  mean tx per block")
    for phase, mean in profile.items():
        mark = "  <== peak" if phase == s["phase"] else ""
        print(f"{phase:>5}  {mean:>8.1f}{mark}")
    print(f"\nPeak at timestamp % {period} == {s['phase']}: "
          f"{s['peak_mean']:.1f} tx per block vs {s['other_mean']:.1f} for the "
          f"other phases ({s['ratio']:.1f}x)")


if __name__ == "__main__":
    main()