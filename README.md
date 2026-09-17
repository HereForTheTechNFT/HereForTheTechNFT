# Here For The Tech

### Digital ownership, zero-knowledge systems and secure onchain infrastructure

I research blockchain protocols through source-grounded technical notes. My work connects NFT infrastructure with ZK proofs, confidential execution, Base and HyperEVM.

## Parcours français

Le [parcours français](docs/fr/README.md) présente 73 notes courtes, chacune consacrée à un mécanisme identifiable dans les sources ou les prototypes de ce dépôt. Il distingue les garanties cryptographiques, les hypothèses opérationnelles et les limites documentaires.

## Featured work

| Area | Repository | Focus |
| --- | --- | --- |
| HyperEVM | [hyperevm-tools](https://github.com/HereForTheTechNFT/hyperevm-tools/tree/main/docs/fr) | L1Read, CoreWriter, cross-DEX transfers, supply synchronization and defensive invariants |
| Hyperliquid | [hyperliquid-python-sdk](https://github.com/HereForTheTechNFT/hyperliquid-python-sdk/tree/master/docs/fr) | Signatures, nonces, partial failures, retries and reconciliation |
| HyperEVM data | [hyper-evm-sync](https://github.com/HereForTheTechNFT/hyper-evm-sync/tree/main/docs/fr) | Replay, snapshots, continuity checks and precompile context |
| Base | [base-std](https://github.com/HereForTheTechNFT/base-std/tree/main/docs/fr) | L1 context, Superchain identity, P256 passkeys and NFT anti-replay rules |
| STARK | [Plonky2](https://github.com/HereForTheTechNFT/plonky2/tree/main/docs/fr) | Goldilocks field, FRI, constraints and recursion |
| SNARK | [Groth16](https://github.com/HereForTheTechNFT/groth16/tree/master/docs/fr) | R1CS, parameters, proving keys, public inputs and pairings |
| FHE | [FHEVM](https://github.com/HereForTheTechNFT/fhevm/tree/main/docs/fr) | Encrypted handles, ACL, coprocessor, KMS and gateway trust boundaries |

## NFT and digital ownership

- [Zora Protocol](https://github.com/HereForTheTechNFT/zora-protocol) — NFT protocol architecture.
- [Nouns DAO](https://github.com/HereForTheTechNFT/nouns-monorepo) — auctions, treasury and governance.
- [Rarible Protocol](https://github.com/HereForTheTechNFT/protocol-contracts) — marketplace contracts and exchange flows.
- [Lens Protocol](https://github.com/HereForTheTechNFT/core) — onchain social ownership.

## Current contribution focus

- Safe interactions between HyperEVM contracts and HyperCore state.
- Passkey authorization and replay resistance for NFT applications on Base.
- Clear separation between cryptographic guarantees, operational assumptions and application policy.
- Reproducible French-language documentation linked to verifiable source mechanisms.

## Method

I read the source, isolate one mechanism per chapter and make trust assumptions and failure modes explicit. These repositories contain documentary analyses: they are not security audits, endorsements or claims of production readiness. No test result is claimed when no test was executed.
