# Fee model

A transaction on Base pays two parts:
1. L2 execution fee: gas used multiplied by the L2 gas price (very low on Base).
2. L1 data fee: the cost of posting the transaction data to Ethereum.

- Since Ethereum introduced blobs (EIP-4844), the L1 data cost for rollups dropped a lot.
- `scripts/compare_fees.py` measures only the L2 part, so the real gap versus Ethereum L1 is slightly smaller than the printed ratio.
- First measurement (2026-09-29): Ethereum L1 was about 127x more expensive than Base for a simple transfer.

## Open questions
- How big is the L1 data fee for a typical transaction on Base?
- How does the fee ratio change during busy periods on Ethereum?
