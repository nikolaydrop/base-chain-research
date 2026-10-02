import os
import sys
from unittest.mock import MagicMock

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from compare_fees import cost_ratio, snapshot  # noqa: E402


def fake_w3(chain_id, block_number, base_fee_wei, gas_price_wei):
    w3 = MagicMock()
    w3.eth.chain_id = chain_id
    w3.eth.get_block.return_value = {
        "number": block_number,
        "baseFeePerGas": base_fee_wei,
    }
    w3.eth.gas_price = gas_price_wei
    return w3


def test_snapshot_computes_transfer_cost():
    s = snapshot(fake_w3(8453, 100, 5_000_000, 10**9))
    assert s["chain_id"] == 8453
    assert s["block"] == 100
    assert float(s["gas_price_gwei"]) == pytest.approx(1.0)
    assert float(s["cost_eth"]) == pytest.approx(21_000 * 10**9 / 10**18)


def test_cost_ratio():
    base = {"cost_eth": 2}
    eth = {"cost_eth": 300}
    assert cost_ratio(base, eth) == 150


def test_cost_ratio_none_when_base_is_zero():
    assert cost_ratio({"cost_eth": 0}, {"cost_eth": 5}) is None