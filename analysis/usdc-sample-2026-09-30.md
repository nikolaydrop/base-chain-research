# USDC transfers on Base: second sample

Run date: 2026-09-30

Script: `scripts/usdc_transfers.py 10` (10 blocks starting at block 51976982, about 20 seconds)

Compare with the first sample: `usdc-sample-2026-09-29.md`

| Metric | Value |
|---|---|
| USDC Transfer events | 1494 |
| Total moved | 50,776,966.92 USDC |
| Unique senders | 337 |
| Unique receivers | 351 |

Top senders by amount (shortened addresses):

| Sender | USDC sent |
|---|---|
| 0xb2cc...DC59 | 18,719,753.14 |
| 0x787f...35E4 | 12,401,257.81 |
| 0x9eef...Eb79 | 6,946,352.94 |
| 0x6104...D14b | 5,054,411.75 |
| 0x4e96...E778 | 3,424,080.15 |

## Observations
- About 75 transfers per second (1494 transfers in roughly 20 seconds), higher than the first sample (about 65 per second).
- Value is highly concentrated: the top 5 senders account for about 92% of the total (46.5M of 50.8M USDC), out of 337 unique senders.
- Several shortened addresses appear in both samples (for example 0xb2cc...DC59, 0x6104...D14b, 0xb300...028d and 0x6aba...1b90). This fits a few high-volume addresses, but the owners are not verified yet.
- "Total moved" still overcounts real volume, because chained transfers (A -> B -> C with the same amount) are counted at every step.

## Limitations
- Two short samples from two different moments, not a daily average.
- Addresses are shortened, so matches between samples are not fully confirmed.

## Next steps
- Look up the top sender addresses on a block explorer such as basescan.org to see whether they are exchanges, routers or other contracts.
- Repeat the run over a longer window and check whether the concentration holds.
