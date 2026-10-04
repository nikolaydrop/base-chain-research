import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from block_stats import percentile, summarize  # noqa: E402


def test_percentile_nearest_rank():
    values = list(range(1, 101))  # 1..100
    assert percentile(values, 50) == 50
    assert percentile(values, 90) == 90
    assert percentile(values, 99) == 99
    assert percentile(values, 100) == 100


def test_percentile_unsorted_and_small_lists():
    assert percentile([5, 1, 3], 100) == 5
    assert percentile([7], 99) == 7
    assert percentile([4, 8], 0) == 4


def test_percentile_empty_raises():
    with pytest.raises(ValueError):
        percentile([], 90)


def test_summarize_includes_median_and_percentiles():
    rows = [
        {"block": str(i), "timestamp": str(1000 + 2 * i), "tx_count": str(i + 1),
         "gas_used": "10", "gas_limit": "100"}
        for i in range(10)
    ]
    s = summarize(rows)
    assert s["tx_median"] == pytest.approx(5.5)
    assert s["tx_p90"] == 9
    assert s["tx_p99"] == 10