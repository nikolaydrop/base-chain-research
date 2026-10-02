import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from latest_block import describe_block  # noqa: E402


def make_block():
    return {
        "number": 123,
        "timestamp": 1_800_000_000,
        "transactions": [0] * 5,
        "gasUsed": 1_500_000,
        "gasLimit": 400_000_000,
        "baseFeePerGas": 5_000_000,
    }


def test_describe_block_has_expected_lines():
    lines = describe_block(make_block(), 8453)
    assert lines[0].endswith("8453")
    assert lines[1].endswith("123")
    assert "2027-01-15 08:00:00" in lines[2]
    assert lines[3].endswith("5")
    assert "1,500,000 / 400,000,000" in lines[4]
    assert "0.005000 gwei" in lines[5]


def test_describe_block_without_base_fee():
    block = make_block()
    del block["baseFeePerGas"]
    assert "0.000000 gwei" in describe_block(block, 1)[5]