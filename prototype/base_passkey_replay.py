#!/usr/bin/env python3
"""Toy passkey replay-resistance model for Base applications."""

from dataclasses import dataclass

@dataclass
class Challenge:
    nonce: str
    used: bool = False

def consume(challenge: Challenge, nonce: str) -> bool:
    if challenge.used or challenge.nonce != nonce:
        return False
    challenge.used = True
    return True

if __name__ == "__main__":
    c = Challenge("session-1")
    print(consume(c, "session-1"), consume(c, "session-1"))
