import json
import os
import sys
from decimal import Decimal

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from compare_fees import parse_args, result_to_dict, snapshot_to_dict  # noqa: E402


def make_snapshot(chain_id, cost_eth):
    return {
        "chain_id": chain_id,
        "block": 100,
        "base_fee_gwei": Decimal("0.005"),
        "gas_price_gwei": Decimal("0.006"),
        "cost_eth": Decimal(cost_eth),
    }


def test_snapshot_to_dict_uses_plain_floats():
    d = snapshot_to_dict(make_snapshot(8453, "0.000000126"))
    assert d["chain_id"] == 8453
    assert isinstance(d["gas_price_gwei"], float)
    assert d["transfer_cost_eth"] == 0.000000126


def test_result_to_dict_has_ratio():
    d = result_to_dict(make_snapshot(8453, "0.000001"), make_snapshot(1, "0.000127"))
    assert d["ethereum_to_base_cost_ratio"] == 127.0
    assert d["base"]["chain_id"] == 8453
    assert d["ethereum"]["chain_id"] == 1


def test_result_to_dict_ratio_is_null_when_base_is_free():
    d = result_to_dict(make_snapshot(8453, "0"), make_snapshot(1, "0.000127"))
    assert d["ethereum_to_base_cost_ratio"] is None


def test_result_is_json_serializable():
    d = result_to_dict(make_snapshot(8453, "0.000001"), make_snapshot(1, "0.000127"))
    assert json.loads(json.dumps(d))["ethereum"]["block"] == 100


def test_parse_args_json_flag():
    assert parse_args(["--json"]).json is True
    assert parse_args([]).json is False