# Usage guide

Install once:
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

All scripts are read-only. They need no wallet and no private keys. Set `BASE_RPC_URL` to use your own RPC endpoint instead of the public one.

## latest_block.py
```bash
python scripts/latest_block.py
```
Example output (2026-09-29):
```
Chain ID:     8453
Block:        51938091
Time (UTC):   2026-09-29 07:05:29+00:00
Transactions: 227
Gas used:     41,947,281 / 400,000,000
Base fee:     0.005000 gwei
```

## block_times.py
```bash
python scripts/block_times.py 20
```
Example output:
```
Blocks checked:   20
Average interval: 2.00 s
Min / max:        2 / 2 s
```

## usdc_transfers.py
```bash
python scripts/usdc_transfers.py 10
python scripts/usdc_transfers.py 10 --full
python scripts/usdc_transfers.py 10 --json
```
Example summary (2026-09-30 sample):
```
Blocks scanned:    10
USDC transfers:    1494
Total moved:       50,776,966.92 USDC
Unique senders:    337
Unique receivers:  351
Top senders by amount:
  0xb2cc...DC59  18,719,753.14 USDC
  0x787f...35E4  12,401,257.81 USDC
  0x9eef...Eb79  6,946,352.94 USDC
  0x6104...D14b  5,054,411.75 USDC
  0x4e96...E778  3,424,080.15 USDC
```
`--full` prints full addresses. `--json` prints only the summary as JSON.

## compare_fees.py
```bash
python scripts/compare_fees.py
python scripts/compare_fees.py --json
```
Example output (2026-09-29):
```
Base (chain 8453, block 51939043)
  Base fee:            0.005000 gwei
  Gas price:           0.006000 gwei
  Simple transfer:     0.0000001260 ETH

Ethereum L1 (chain 1, block 26081672)
  Base fee:            0.759579 gwei
  Gas price:           0.759636 gwei
  Simple transfer:     0.0000159524 ETH

Ethereum L1 is about 127x more expensive than Base right now.
```
On Base only the L2 execution fee is counted, so the real gap is somewhat smaller.

## export_blocks.py, block_stats.py and plot_blocks.py
```bash
python scripts/export_blocks.py 500 data/blocks-500.csv
python scripts/block_stats.py data/blocks-500.csv
python scripts/plot_blocks.py data/blocks-500.csv analysis/blocks-500.png
```
Example output of `block_stats.py`:
```
Blocks:            500 (52108779 to 52109278)
Block interval:    2.00 s
Transactions:      79,758 total, 160 per block (min 105, max 345)
Per block:         median 148, p90 205, p99 305
Throughput:        about 80 tx/s
Gas utilization:   9.6% average, 19.5% max
```

## fee_history.py
```bash
python scripts/fee_history.py 100
```
Example output (2026-10-05):
```
Blocks:          100 (52191330 to 52191429)
Base fee min:    0.005000 gwei
Base fee max:    0.005000 gwei
Base fee avg:    0.005000 gwei
Gas used (avg):  8.1% of the block limit
```

## Tests
```bash
pip install -r requirements-dev.txt
python -m pytest
```