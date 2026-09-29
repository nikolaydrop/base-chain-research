"""Average time between blocks over the last N blocks (default: 50)."""
import os
import sys

from web3 import Web3

RPC_URL = os.getenv("BASE_RPC_URL", "https://mainnet.base.org")


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    latest = w3.eth.block_number

    timestamps = [w3.eth.get_block(latest - i)["timestamp"] for i in range(n + 1)]
    deltas = [timestamps[i] - timestamps[i + 1] for i in range(n)]

    print(f"Blocks checked:   {n}")
    print(f"Average interval: {sum(deltas) / n:.2f} s")
    print(f"Min / max:        {min(deltas)} / {max(deltas)} s")


if __name__ == "__main__":
    main()
