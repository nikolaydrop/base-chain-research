# What is an L2 and a rollup

- An L2 (layer 2) executes transactions off Ethereum mainnet and posts the transaction data back to Ethereum (L1), so it inherits L1 security while being cheaper and faster.
- A rollup "rolls up" many transactions into a batch and publishes that batch to L1.
- Optimistic rollups assume batches are valid and allow a challenge period for fraud proofs. Base is an optimistic rollup built on the OP Stack.
- ZK rollups publish a validity proof with each batch, so no challenge period is needed.

## Answered questions
- How long does a withdrawal from Base to Ethereum take, and why? A standard withdrawal can be finalized on Ethereum only after a 7 day challenge period, which gives participants time to dispute an invalid output root. Deposits and regular transactions on Base do not wait that long. Details: `07-bridge.md`.

## Open questions
- How much does the L1 data fee contribute to a typical Base transaction?