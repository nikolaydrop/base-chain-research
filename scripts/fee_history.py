"""Summarize the recent base fee history on Base (eth_feeHistory).

Usage: python scripts/fee_history.py [N_BLOCKS]
Default: 100 blocks. Read-only, no wallet required.
"""
import sys

from web3 import Web3

from rpc import connect, with_retry


def summarize_history(history):
    """Min, max and average base fee (gwei) and average gas used ratio."""
    fees = [Web3.from_wei(f, "gwei") for f in history["baseFeePerGas"]]
    ratios = history["gasUsedRatio"]
    if not fees or not ratios:
        raise ValueError("empty fee history")
    return {
        "oldest_block": history["oldestBlock"],
        "blocks": len(ratios),
        "base_fee_min_gwei": float(min(fees)),
        "base_fee_max_gwei": float(max(fees)),
        "base_fee_avg_gwei": float(sum(fees) / len(fees)),
        "gas_used_avg_pct": 100 * sum(ratios) / len(ratios),
    }


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    if n < 1:
        raise SystemExit("N_BLOCKS must be at least 1")

    w3 = connect()
    history = with_retry(w3.eth.fee_history, n, "latest")
    s = summarize_history(history)

    last = s["oldest_block"] + s["blocks"] - 1
    print(f"Blocks:          {s['blocks']} ({s['oldest_block']} to {last})")
    print(f"Base fee min:    {s['base_fee_min_gwei']:.6f} gwei")
    print(f"Base fee max:    {s['base_fee_max_gwei']:.6f} gwei")
    print(f"Base fee avg:    {s['base_fee_avg_gwei']:.6f} gwei")
    print(f"Gas used (avg):  {s['gas_used_avg_pct']:.1f}% of the block limit")


if __name__ == "__main__":
    main()