"""Fetch the latest Base block. Read-only, no wallet required."""
from datetime import datetime, timezone

from web3 import Web3

from rpc import connect, with_retry


def describe_block(block, chain_id):
    """Return printable lines describing a block."""
    ts = datetime.fromtimestamp(block["timestamp"], tz=timezone.utc)
    base_fee_gwei = Web3.from_wei(block.get("baseFeePerGas", 0), "gwei")
    return [
        f"Chain ID:     {chain_id}",
        f"Block:        {block['number']}",
        f"Time (UTC):   {ts}",
        f"Transactions: {len(block['transactions'])}",
        f"Gas used:     {block['gasUsed']:,} / {block['gasLimit']:,}",
        f"Base fee:     {base_fee_gwei:.6f} gwei",
    ]


def main():
    w3 = connect()
    block = with_retry(w3.eth.get_block, "latest")
    for line in describe_block(block, w3.eth.chain_id):
        print(line)


if __name__ == "__main__":
    main()