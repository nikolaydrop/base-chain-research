# USDC transfers on Base: first sample

Run date: 2026-09-29
Script: `scripts/usdc_transfers.py` (10 blocks, starting at block 51938446)

| Metric | Value |
|---|---|
| Blocks scanned | 10 (~20 seconds) |
| USDC Transfer events | 1296 |
| Total moved | 17,646,614.57 USDC |

## Observations
- About 65 USDC transfers per second on Base at this moment.
- Amounts range from ~1 USDC to over 130,000 USDC.
- Several transfers repeat the same amount in a chain (A -> B -> C), which suggests routing through intermediary contracts.
- "Total moved" overcounts real volume, because one payment can generate several Transfer events.

## Next questions
- How many unique senders and receivers are there in a longer window?
- How does this activity change by hour of day?
