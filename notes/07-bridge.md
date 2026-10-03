# Bridging between Ethereum and Base

Sources: Base documentation, pages "Bridging and Withdrawals" and "Transaction Finality" (docs.base.org).
Checked on 2026-10-03. Details can change, so re-check before relying on them.

## Ethereum to Base (deposit)
- A deposit is started on Ethereum and picked up by the Base sequencer.
- Typical inclusion time according to the docs: about 3 minutes.
- Deposits do not have the 7 day wait.

## Base to Ethereum (standard withdrawal)
Three steps:
1. Initiate: send the withdrawal transaction on Base.
2. Prove: once the relevant Base state has been posted to Ethereum, anyone can submit a proof to the OptimismPortal contract on Ethereum.
3. Finalize: after the 7 day challenge period, anyone can finalize the withdrawal on Ethereum.

Why 7 days: the proof relies on an output root that commits to Base state. The challenge period gives participants time to dispute an invalid output root before withdrawals that depend on it can be finalized.

## Faster options
- Some third-party bridge providers offer faster withdrawals.
- According to the docs they usually do not shorten the underlying 7 day challenge period of the standard bridge.

## Takeaways
- Only withdrawals to Ethereum wait 7 days. Regular transactions on Base and deposits do not.
- Proving and finalizing can be done by any address, so wallets or other services can complete these steps for the user.

## Open questions
- Which bridge providers offer faster withdrawals, and what extra trust assumptions do they add?
- How does the fault proof system decide the outcome of a challenge?