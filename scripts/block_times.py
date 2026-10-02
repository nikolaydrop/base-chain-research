"""Average time between blocks over the last N blocks (default: 50)."""
import sys

from rpc import connect, with_retry


def intervals(timestamps):
    """Gaps in seconds between consecutive timestamps (newest first)."""
    return [timestamps[i] - timestamps[i + 1] for i in range(len(timestamps) - 1)]


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    if n < 1:
        raise SystemExit("N must be at least 1")

    w3 = connect()
    latest = w3.eth.block_number
    timestamps = [
        with_retry(w3.eth.get_block, latest - i)["timestamp"] for i in range(n + 1)
    ]
    deltas = intervals(timestamps)

    print(f"Blocks checked:   {n}")
    print(f"Average interval: {sum(deltas) / n:.2f} s")
    print(f"Min / max:        {min(deltas)} / {max(deltas)} s")


if __name__ == "__main__":
    main()