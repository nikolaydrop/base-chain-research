"""Small helpers for talking to a Base RPC endpoint (read-only)."""
import os
import time

from web3 import Web3

DEFAULT_RPC = "https://mainnet.base.org"


def rpc_url():
    """RPC endpoint from BASE_RPC_URL, or the public Base endpoint."""
    return os.getenv("BASE_RPC_URL", DEFAULT_RPC)


def connect(url=None):
    """Return a connected Web3 instance or exit with a clear message."""
    url = url or rpc_url()
    w3 = Web3(Web3.HTTPProvider(url, request_kwargs={"timeout": 15}))
    if not w3.is_connected():
        raise SystemExit(f"Could not connect to {url}")
    return w3


def with_retry(func, *args, attempts=3, delay=1.0, sleep=time.sleep, **kwargs):
    """Call func(*args, **kwargs), retrying on errors with a growing delay."""
    for attempt in range(1, attempts + 1):
        try:
            return func(*args, **kwargs)
        except Exception:
            if attempt == attempts:
                raise
            sleep(delay * attempt)