import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from usdc_transfers import format_address, parse_args  # noqa: E402

ADDR = "0x" + "ab" * 20


def test_format_address_shortens_by_default():
    assert format_address(ADDR) == "0xabab...abab"


def test_format_address_full():
    assert format_address(ADDR, full=True) == ADDR


def test_parse_args_defaults():
    args = parse_args([])
    assert args.blocks == 10
    assert args.full is False


def test_parse_args_blocks_and_full_flag():
    args = parse_args(["25", "--full"])
    assert args.blocks == 25
    assert args.full is True
