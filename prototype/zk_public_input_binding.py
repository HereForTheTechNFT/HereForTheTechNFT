#!/usr/bin/env python3
"""Toy transcript binding for a ZK proof public-input set."""

from hashlib import sha256

def transcript_digest(statement: str, public_inputs: list[str]) -> str:
    payload = "zk-demo/v1|" + statement + "|" + "|".join(public_inputs)
    return sha256(payload.encode()).hexdigest()

if __name__ == "__main__":
    print(transcript_digest("balance", ["alice", "10"]))
