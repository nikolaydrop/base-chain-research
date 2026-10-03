import csv
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from export_blocks import FIELDS, block_row, write_csv  # noqa: E402


def make_block(number=100):
    return {
        "number": number,
        "timestamp": 1_800_000_000 + number,
        "transactions": [0] * 7,
        "gasUsed": 1000,
        "gasLimit": 2000,
        "baseFeePerGas": 5_000_000,
    }


def test_block_row_field_order():
    assert block_row(make_block()) == [100, 1_800_000_100, 7, 1000, 2000, 5_000_000]


def test_block_row_defaults_base_fee_to_zero():
    block = make_block()
    del block["baseFeePerGas"]
    assert block_row(block)[-1] == 0


def test_write_csv_creates_folder_and_header(tmp_path):
    out = tmp_path / "nested" / "blocks.csv"
    write_csv(str(out), [block_row(make_block(1)), block_row(make_block(2))])
    with open(out, newline="") as f:
        rows = list(csv.reader(f))
    assert rows[0] == FIELDS
    assert len(rows) == 3
    assert rows[1][0] == "1"