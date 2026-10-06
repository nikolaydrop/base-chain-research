import csv
import glob
import os

import pytest

DATA_DIR = os.path.join(os.path.dirname(__file__), "..", "data")
EXPECTED_HEADER = [
    "block", "timestamp", "tx_count", "gas_used", "gas_limit", "base_fee_wei",
]
CSV_FILES = sorted(glob.glob(os.path.join(DATA_DIR, "blocks*.csv")))


def read_rows(path):
    with open(path, newline="") as f:
        return list(csv.DictReader(f))


@pytest.mark.parametrize("path", CSV_FILES)
def test_header_is_expected(path):
    with open(path, newline="") as f:
        assert next(csv.reader(f)) == EXPECTED_HEADER


@pytest.mark.parametrize("path", CSV_FILES)
def test_block_numbers_are_consecutive(path):
    blocks = [int(r["block"]) for r in read_rows(path)]
    assert all(b - a == 1 for a, b in zip(blocks, blocks[1:]))


@pytest.mark.parametrize("path", CSV_FILES)
def test_timestamps_do_not_decrease(path):
    stamps = [int(r["timestamp"]) for r in read_rows(path)]
    assert all(b >= a for a, b in zip(stamps, stamps[1:]))


@pytest.mark.parametrize("path", CSV_FILES)
def test_gas_used_never_exceeds_limit(path):
    for r in read_rows(path):
        assert int(r["gas_used"]) <= int(r["gas_limit"])