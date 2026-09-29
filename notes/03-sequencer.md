# The sequencer

- The sequencer receives user transactions, orders them, and produces L2 blocks.
- On Base a new block appears every 2 seconds (measured with `scripts/block_times.py`).
- The sequencer also posts batches of transaction data to Ethereum L1.
- Sequencing is centralized: one operator controls ordering. Check docs.base.org for the current state.
- If the sequencer misbehaves, users can still submit transactions through L1 (forced inclusion), but this is slower.

## Open questions
- Who operates the Base sequencer, and are there plans to decentralize it?
- What happens to users if the sequencer goes offline?
