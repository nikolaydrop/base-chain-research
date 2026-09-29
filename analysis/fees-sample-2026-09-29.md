# Fee comparison: Base vs Ethereum L1

Run date: 2026-09-29

Script: `scripts/compare_fees.py`

| | Base | Ethereum L1 |
|---|---|---|
| Chain ID | 8453 | 1 |
| Block | 51939043 | 26081672 |
| Base fee | 0.005000 gwei | 0.759579 gwei |
| Gas price | 0.006000 gwei | 0.759636 gwei |
| Simple transfer (21,000 gas) | 0.0000001260 ETH | 0.0000159524 ETH |

Result: Ethereum L1 was about 127x more expensive than Base at this moment.

## Notes
- The Base figure covers only the L2 execution fee. The L1 data fee (posting data to Ethereum) is not included, so the real gap is somewhat smaller.
- Ethereum gas was unusually low (below 1 gwei) during this run. On busy days the gap would be much larger.
- Base fee on Base was 0.005 gwei in both runs today, which suggests low congestion.

## Next questions
- How does the ratio change over a full day?
- How large is the L1 data fee compared to the L2 execution fee?
