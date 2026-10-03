# The sequencer

- The sequencer receives user transactions, orders them, and produces L2 blocks.
- On Base a new block appears every 2 seconds (measured with `scripts/block_times.py`).
- The sequencer also posts batches of transaction data to Ethereum L1. According to the Base docs, a batch containing a given transaction is on Ethereum after roughly 2 minutes.
- Sequencing is centralized: the Base docs say Base currently operates with a single active sequencer (checked on 2026-10-03).
- Users can submit transactions through the sequencer or by interacting with contracts on Ethereum.

## Open questions
- Who operates the Base sequencer, and are there plans to decentralize it?
- What happens to users if the sequencer goes offline?