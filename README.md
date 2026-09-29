# base-chain-research

Research of the Base blockchain (Coinbase's L2 built on the OP Stack) using real on-chain data.

## Goals
- Understand Base architecture: rollup, sequencer, bridge, and fee model
- Collect network data through a public RPC (read-only)
- Compare fees and block times with Ethereum L1

## Security
This project is **read-only**: no wallet, private keys, or seed phrases are used or required.

## Quick start
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/latest_block.py
python scripts/block_times.py 50
```

## Project structure
- `notes/` study notes
- `scripts/` scripts for querying the network
- `data/` data exports
- `analysis/` reports and charts

## Network parameters
| | Mainnet | Sepolia (testnet) |
|---|---|---|
| Chain ID | 8453 | 84532 |
| RPC | https://mainnet.base.org | https://sepolia.base.org |
