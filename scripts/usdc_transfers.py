"""Show recent USDC Transfer events on Base. Read-only, no wallet required.

Usage: python scripts/usdc_transfers.py [N_BLOCKS] [--full]
  N_BLOCKS  how many recent blocks to scan (default: 10)
  --full    print full addresses instead of shortened ones
"""
import argparse
import os
from collections import defaultdict

from web3 import Web3

RPC_URL = os.getenv("BASE_RPC_URL", "https://mainnet.base.org")
USDC = "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913"  # native USDC on Base
TRANSFER_TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
DECIMALS = 6


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description="Recent USDC transfers on Base")
    parser.add_argument("blocks", nargs="?", type=int, default=10,
                        help="number of recent blocks to scan (default: 10)")
    parser.add_argument("--full", action="store_true",
                        help="print full addresses instead of shortened ones")
    return parser.parse_args(argv)


def format_address(addr, full=False):
    """Return the address as is, or shortened like 0x1234...abcd."""
    return addr if full else f"{addr[:6]}...{addr[-4:]}"


def to_address(topic):
    """Convert a 32-byte indexed topic into a checksummed address."""
    return Web3.to_checksum_address(bytes(topic)[-20:])


def decode_transfer(log):
    """Turn a raw Transfer log into a simple dict."""
    return {
        "block": log["blockNumber"],
        "from": to_address(log["topics"][1]),
        "to": to_address(log["topics"][2]),
        "amount": int.from_bytes(bytes(log["data"]), "big") / 10**DECIMALS,
    }


def summarize(transfers, top_n=5):
    """Count transfers, unique addresses and the biggest senders."""
    sent = defaultdict(float)
    receivers = set()
    for t in transfers:
        sent[t["from"]] += t["amount"]
        receivers.add(t["to"])
    top = sorted(sent.items(), key=lambda kv: kv[1], reverse=True)[:top_n]
    return {
        "count": len(transfers),
        "total": sum(t["amount"] for t in transfers),
        "unique_senders": len(sent),
        "unique_receivers": len(receivers),
        "top_senders": top,
    }


def main():
    args = parse_args()
    w3 = Web3(Web3.HTTPProvider(RPC_URL))
    if not w3.is_connected():
        raise SystemExit(f"Could not connect to {RPC_URL}")

    latest = w3.eth.block_number
    logs = w3.eth.get_logs({
        "fromBlock": latest - args.blocks + 1,
        "toBlock": latest,
        "address": Web3.to_checksum_address(USDC),
        "topics": [TRANSFER_TOPIC],
    })
    transfers = [decode_transfer(log) for log in logs if len(log["topics"]) == 3]

    for t in transfers[:15]:
        sender = format_address(t["from"], args.full)
        receiver = format_address(t["to"], args.full)
        print(f"block {t['block']}: {sender} -> {receiver}  {t['amount']:,.2f} USDC")

    s = summarize(transfers)
    print(f"\nBlocks scanned:    {args.blocks}")
    print(f"USDC transfers:    {s['count']}")
    print(f"Total moved:       {s['total']:,.2f} USDC")
    print(f"Unique senders:    {s['unique_senders']}")
    print(f"Unique receivers:  {s['unique_receivers']}")
    print("Top senders by amount:")
    for addr, amount in s["top_senders"]:
        print(f"  {format_address(addr, args.full)}  {amount:,.2f} USDC")


if __name__ == "__main__":
    main()
