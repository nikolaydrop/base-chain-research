# Base fee history: 100 blocks

Run date: 2026-10-05

Script: `scripts/fee_history.py 100`

Saved output: `data/fee-history-2026-10-05.txt`

| Metric | Value |
|---|---|
| Blocks | 100 (52191330 to 52191429) |
| Base fee, minimum / maximum / average | 0.005000 gwei in every block |
| Gas used, average | 8.1% of the block limit |

## Observations
- The base fee did not move at all in this window: minimum, maximum and average are the same.
- According to the Base docs, Base Mainnet has a minimum base fee of 5,000,000 wei (0.005 gwei), so a constant value of 0.005 gwei means the fee sits at its floor.
- The same value (0.005 gwei) appeared in the earlier samples of 2026-09-30 (100 blocks) and 2026-10-03 (500 blocks). Average gas use in the three samples was 11%, 9.6% and 8.1%.
- With blocks this far from full, there is no upward pressure on the base fee.

## Limitations
- Short windows at calm moments. They say little about how the fee behaves during bursts of activity.
- Only the L2 base fee is covered here. The L1 data fee is a separate part of what users pay.

## Next questions
- What does the base fee do when blocks fill up? The docs list a maximum change of 4% per block.
- How large is the L1 data fee compared with the L2 execution fee?