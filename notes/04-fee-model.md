# Fee model

A transaction on Base pays two parts:
1. L2 execution fee: gas used multiplied by the L2 gas price (very low on Base).
2. L1 data fee: the cost of posting the transaction data to Ethereum.

- Since Ethereum introduced blobs (EIP-4844), the L1 data cost for rollups dropped a lot.
- `scripts/compare_fees.py` measures only the L2 part, so the real gap versus Ethereum L1 is slightly smaller than the printed ratio.
- First measurement (2026-09-29): Ethereum L1 was about 127x more expensive than Base for a simple transfer.

## Minimum base fee
- Base has a minimum base fee that works as a floor for the L2 base fee. The Base docs say it was introduced with the Jovian upgrade and is 5,000,000 wei (0.005 gwei) on Base Mainnet.
- The docs say the value may be adjusted over time.
- In all samples collected here (2026-09-30, 2026-10-03, 2026-10-05) the base fee sat exactly at this floor.
- The EIP-1559 parameters listed in the docs for Base Mainnet: elasticity 6, denominator 125, so the base fee changes by at most 4% per block.

## Open questions
- How big is the L1 data fee for a typical transaction on Base?
- How does the fee ratio change during busy periods on Ethereum?
- What does the base fee do when blocks fill up?