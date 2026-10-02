import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))

from rpc import with_retry  # noqa: E402


def test_with_retry_returns_value_on_first_success():
    assert with_retry(lambda x: x * 2, 21, sleep=lambda s: None) == 42


def test_with_retry_recovers_after_failures():
    calls = {"n": 0}
    delays = []

    def flaky():
        calls["n"] += 1
        if calls["n"] < 3:
            raise RuntimeError("temporary error")
        return "ok"

    assert with_retry(flaky, attempts=3, delay=1.0, sleep=delays.append) == "ok"
    assert calls["n"] == 3
    assert delays == [1.0, 2.0]


def test_with_retry_raises_after_last_attempt():
    calls = {"n": 0}

    def always_fails():
        calls["n"] += 1
        raise RuntimeError("down")

    with pytest.raises(RuntimeError):
        with_retry(always_fails, attempts=3, sleep=lambda s: None)
    assert calls["n"] == 3