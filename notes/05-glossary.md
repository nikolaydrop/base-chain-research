# Glossary

- **L1 / L2**: layer 1 (Ethereum mainnet) and layer 2 (a chain built on top of it, such as Base).
- **Rollup**: an L2 that posts transaction data to L1.
- **Sequencer**: the service that orders transactions and produces L2 blocks.
- **RPC**: the endpoint used to read data from a blockchain node.
- **Gas**: the unit that measures the computation a transaction needs.
- **Gwei**: one billionth of an ETH, the usual unit for gas prices.
- **Base fee**: the minimum per-gas price required for a transaction to be included.
- **ERC-20**: the standard interface for fungible tokens such as USDC.
- **Transfer event**: the log emitted by an ERC-20 contract when tokens move.
- **Blob (EIP-4844)**: a cheap data format on Ethereum that rollups use to post their data.
- **Challenge period**: the 7 day wait before a standard withdrawal from Base can be finalized on Ethereum.
- **Output root**: a commitment to the state of Base that withdrawals are proven against. It can be disputed during the challenge period.
- **Minimum base fee**: a floor for the L2 base fee. According to the Base docs it is 0.005 gwei on Base Mainnet.
- **EIP-1559**: the fee mechanism with a base fee that adjusts from block to block plus an optional tip.
- **Percentile**: the value below which a given share of observations fall. Used here for transactions per block.
