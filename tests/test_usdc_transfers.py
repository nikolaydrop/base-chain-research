import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from usdc_transfers import decode_transfer, summarize, to_address  # noqa: E402

ALICE = "0x" + "11" * 20
BOB = "0x" + "22" * 20
CAROL = "0x" + "33" * 20


def topic(addr_hex):
    return bytes(12) + bytes.fromhex(addr_hex[2:])


def make_log(sender, receiver, units, block=100):
    return {
        "blockNumber": block,
        "topics": [b"\xdd", topic(sender), topic(receiver)],
        "data": units.to_bytes(32, "big"),
    }


def test_to_address_takes_last_20_bytes():
    assert to_address(topic(ALICE)).lower() == ALICE


def test_decode_transfer_amount_uses_6_decimals():
    t = decode_transfer(make_log(ALICE, BOB, 1_234_560))
    assert t["amount"] == pytest.approx(1.23456)
    assert t["block"] == 100
    assert t["from"].lower() == ALICE
    assert t["to"].lower() == BOB


def test_summarize_counts_and_top_senders():
    transfers = [
        decode_transfer(make_log(ALICE, BOB, 5_000_000)),
        decode_transfer(make_log(ALICE, CAROL, 2_000_000)),
        decode_transfer(make_log(BOB, CAROL, 1_000_000)),
    ]
    s = summarize(transfers)
    assert s["count"] == 3
    assert s["total"] == pytest.approx(8.0)
    assert s["unique_senders"] == 2
    assert s["unique_receivers"] == 2
    assert s["top_senders"][0][0].lower() == ALICE
    assert s["top_senders"][0][1] == pytest.approx(7.0)


def test_summarize_empty_list():
    s = summarize([])
    assert s["count"] == 0
    assert s["top_senders"] == []
