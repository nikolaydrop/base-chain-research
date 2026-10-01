# base-chain-research

![tests](https://github.com/nikolaydrop/base-chain-research/actions/workflows/tests.yml/badge.svg)

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

## Scripts

| Script | What it does |
|---|---|
| `scripts/latest_block.py` | Prints details of the latest Base block |
| `scripts/block_times.py [N]` | Average time between the last N blocks |
| `scripts/usdc_transfers.py [N] [--full]` | USDC transfers over the last N blocks with unique addresses and top senders (`--full` prints full addresses) |
| `scripts/compare_fees.py` | Compares simple transfer cost on Base and Ethereum L1 |
| `scripts/export_blocks.py [N] [path]` | Exports stats of the last N blocks to CSV |
| `scripts/plot_blocks.py [csv] [png]` | Draws transactions and gas usage charts from the CSV |
| `scripts/block_stats.py [csv]` | Prints summary stats from the CSV |

## Tests
```bash
pip install -r requirements-dev.txt
python -m pytest
```
