# Top USDC senders on Base: what the explorer shows

Date: 2026-09-30

Source: `scripts/usdc_transfers.py 10 --full` and a block explorer for Base.

Only publicly visible facts are recorded as facts. Interpretations are marked as such.

## 0x9eefB63ff5274358319f15798a13a68CaeF9Eb79

Third largest sender in the second USDC sample (about 6.9M USDC in 10 blocks).

| Property | Value |
|---|---|
| Type | Contract |
| ETH balance | 0 ETH |
| Token holdings | about $629,000 across 9 tokens (at the time of viewing) |
| Created | about 26 days before the check |
| Total transactions | about 970,000 |
| Public name tag | none visible |

### Observations
- Incoming transactions arrive roughly every 2 seconds, all from one sending address (0x356575F2...32F239dc9), with 0 ETH value.
- The calls alternate between two method IDs: 0x07cb82b4 and 0xda6b0e38.
- About 970,000 transactions in about 26 days is roughly one transaction every 2 to 3 seconds on average.
- Interpretation (not confirmed): this pattern is consistent with an automated system such as a bot, but the contract's purpose is unknown.
- It sent about 6.9M USDC in 10 blocks while holding only about $0.6M in tokens, so funds appear to pass through it quickly.

### Open questions
- Is the contract's source code verified on the explorer, and what do the two methods do?
- Is 0x356575F2...32F239dc9 a contract or a regular account?
- What are the other four top senders (0xb2cc...DC59, 0x787f...35E4, 0x6104...D14b, 0x4e96...E778)?
