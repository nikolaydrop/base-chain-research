import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from block_stats import summarize  # noqa: E402


def make_rows():
    return [
        {"block": "100", "timestamp": "1000", "tx_count": "10", "gas_used": "10", "gas_limit": "100"},
        {"block": "101", "timestamp": "1002", "tx_count": "30", "gas_used": "20", "gas_limit": "100"},
        {"block": "102", "timestamp": "1004", "tx_count": "20", "gas_used": "30", "gas_limit": "100"},
    ]


def test_summarize_basic_numbers():
    s = summarize(make_rows())
    assert s["blocks"] == 3
    assert s["first_block"] == 100
    assert s["last_block"] == 102
    assert s["tx_total"] == 60
    assert s["tx_min"] == 10
    assert s["tx_max"] == 30


def test_summarize_interval_and_throughput():
    s = summarize(make_rows())
    assert s["avg_interval_s"] == pytest.approx(2.0)
    assert s["tps"] == pytest.approx(60 / 4)


def test_summarize_gas_utilization():
    s = summarize(make_rows())
    assert s["gas_util_avg_pct"] == pytest.approx(20.0)
    assert s["gas_util_max_pct"] == pytest.approx(30.0)


def test_summarize_needs_two_blocks():
    with pytest.raises(ValueError):
        summarize(make_rows()[:1])
