# Changelog

All notable changes to this project, by date (UTC).

## 2026-10-06
- Added `scripts/periodicity.py` with tests and a report on the repeating 30 second spikes.
- Added EditorConfig, pytest configuration, CSV data quality tests, a usage guide, a summary of all samples and this changelog.
- Extended the glossary and linked the reports from the README.

## 2026-10-05
- Added `scripts/fee_history.py` (base fee history over the last N blocks) with tests.
- Added a report on the base fee history and notes on the minimum base fee.
- Updated the README scripts table.

## 2026-10-04
- Added `--json` output to `usdc_transfers.py` and `compare_fees.py`.
- Added median and percentiles to `block_stats.py` and corrected the percentile values in the 500-block report.

## 2026-10-03
- Moved `export_blocks.py` and `usdc_transfers.py` to the shared RPC helper.
- Collected a 500-block sample with a chart and a report.
- Added notes on bridging and updated the L2 and sequencer notes from the Base docs.

## 2026-10-02
- Added tests for the RPC retry helper.
- Moved `block_times.py`, `latest_block.py` and `compare_fees.py` to the shared RPC helper.

## 2026-10-01
- Added CI that runs the tests on every push and a status badge in the README.
- Added `scripts/rpc.py` (connect and retry helpers).
- Saved a USDC transfers summary with full addresses.

## 2026-09-30
- Added `plot_blocks.py` and `block_stats.py`, tests, and the first 100-block sample with a report.
- Extended `usdc_transfers.py` with unique addresses, top senders and `--full`.
- Added the second USDC sample and notes on a top sender contract.

## 2026-09-29
- Created the repository with the README, requirements and the first scripts: `latest_block.py`, `block_times.py`, `usdc_transfers.py`, `compare_fees.py`, `export_blocks.py`.
- Added study notes (L2 basics, OP Stack, sequencer, fee model, glossary) and the first USDC and fee reports.