#!/usr/bin/env python3
"""Toy lifecycle model for an encrypted FHE handle ACL."""

from dataclasses import dataclass, field

@dataclass
class Handle:
    owner: str
    readers: set[str] = field(default_factory=set)
    active: bool = True

def authorize(handle: Handle, reader: str) -> None:
    if not handle.active:
        raise ValueError("inactive handle")
    handle.readers.add(reader)

def revoke(handle: Handle, reader: str) -> None:
    handle.readers.discard(reader)

if __name__ == "__main__":
    h = Handle("alice")
    authorize(h, "service")
    revoke(h, "service")
    print(h.readers)
