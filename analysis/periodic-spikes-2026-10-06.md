# Repeating spikes in transactions per block

Date: 2026-10-06

Script: `scripts/periodicity.py` (run on `data/blocks.csv` and `data/blocks-500.csv`)

Question from earlier reports: what causes the spikes in transactions per block?

## Result
Blocks whose timestamp satisfies `timestamp % 30 == 3` carry clearly more transactions than the other blocks. In UTC this is second 3 and second 33 of every minute.

| Sample | Mean in the peak block | Mean in other blocks | Ratio |
|---|---|---|---|
| `data/blocks.csv` (100 blocks, 2026-09-30) | 286.7 | 196.6 | 1.5x |
| `data/blocks-500.csv` (500 blocks, 2026-10-03) | 274.2 | 151.4 | 1.8x |

The peak sits at the same position in both samples, which were collected on different days.

## Extra check (not part of a script)
In the 500-block sample, 25 blocks had at least 261 transactions (the 95th percentile). Of the 24 gaps between consecutive such blocks, 12 were exactly 15 blocks (30 seconds), 6 were exactly 30 blocks (60 seconds) and 6 were irregular (5, 13, 13, 17, 25 and 32 blocks).

## Interpretation
- The spikes are not random: they follow a 30 second cycle with a fixed position inside it.
- A recurring process on Base that sends transactions every 30 seconds would fit this pattern. This is a hypothesis. The cause has not been identified.

## Limitations
- Two samples only, both short.
- The check shows when extra transactions appear, not which contracts or accounts send them.

## Next steps
- Open one of the peak blocks on a block explorer and look at what its transactions have in common.
- Repeat the analysis on a longer sample to see whether the pattern holds all day.