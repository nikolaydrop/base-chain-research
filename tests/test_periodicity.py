import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from periodicity import peak_summary, phase_profile  # noqa: E402


def make_rows(pairs):
    return [{"timestamp": str(t), "tx_count": str(n)} for t, n in pairs]


def test_phase_profile_averages_by_phase():
    rows = make_rows([(1, 100), (3, 300), (31, 100), (33, 500), (61, 100)])
    profile = phase_profile(rows, 30)
    assert profile == {1: 100.0, 3: 400.0}


def test_peak_summary_finds_peak_and_ratio():
    s = peak_summary({1: 100.0, 3: 300.0, 5: 100.0})
    assert s["phase"] == 3
    assert s["peak_mean"] == 300.0
    assert s["other_mean"] == pytest.approx(100.0)
    assert s["ratio"] == pytest.approx(3.0)


def test_peak_summary_needs_two_phases():
    with pytest.raises(ValueError):
        peak_summary({1: 100.0})