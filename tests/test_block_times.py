import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from block_times import intervals  # noqa: E402


def test_intervals_newest_first():
    assert intervals([110, 108, 106, 103]) == [2, 2, 3]


def test_intervals_single_timestamp_is_empty():
    assert intervals([100]) == []