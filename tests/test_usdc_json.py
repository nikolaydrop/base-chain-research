import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from usdc_transfers import parse_args, summary_to_dict  # noqa: E402

ALICE = "0x" + "11" * 20
BOB = "0x" + "22" * 20


def make_summary():
    return {
        "count": 3,
        "total": 8.123456,
        "unique_senders": 2,
        "unique_receivers": 2,
        "top_senders": [(ALICE, 7.004), (BOB, 1.119456)],
    }


def test_summary_to_dict_rounds_and_shortens():
    d = summary_to_dict(make_summary(), 10)
    assert d["blocks_scanned"] == 10
    assert d["transfers"] == 3
    assert d["total_usdc"] == 8.12
    assert d["top_senders"][0] == {"address": "0x1111...1111", "usdc": 7.0}


def test_summary_to_dict_full_addresses():
    d = summary_to_dict(make_summary(), 10, full=True)
    assert d["top_senders"][1]["address"] == BOB


def test_summary_to_dict_is_json_serializable():
    text = json.dumps(summary_to_dict(make_summary(), 5))
    assert json.loads(text)["unique_senders"] == 2


def test_parse_args_json_flag():
    assert parse_args(["--json"]).json is True
    assert parse_args([]).json is False