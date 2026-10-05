import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from fee_history import summarize_history  # noqa: E402


def make_history():
    return {
        "oldestBlock": 100,
        "baseFeePerGas": [5_000_000, 5_000_000, 10_000_000],
        "gasUsedRatio": [0.1, 0.3],
    }


def test_summarize_history_base_fees():
    s = summarize_history(make_history())
    assert s["base_fee_min_gwei"] == pytest.approx(0.005)
    assert s["base_fee_max_gwei"] == pytest.approx(0.01)
    assert s["base_fee_avg_gwei"] == pytest.approx(0.02 / 3)


def test_summarize_history_blocks_and_gas_usage():
    s = summarize_history(make_history())
    assert s["oldest_block"] == 100
    assert s["blocks"] == 2
    assert s["gas_used_avg_pct"] == pytest.approx(20.0)


def test_summarize_history_empty_raises():
    with pytest.raises(ValueError):
        summarize_history({"oldestBlock": 1, "baseFeePerGas": [], "gasUsedRatio": []})