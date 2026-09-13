#!/usr/bin/env python3
"""Toy reconciliation model for retried Hyperliquid orders."""

from dataclasses import dataclass

@dataclass
class OrderResult:
    client_id: str
    status: str

def reconcile(sent: list[str], acknowledged: list[str]) -> list[str]:
    seen = set(acknowledged)
    return [client_id for client_id in sent if client_id not in seen]

if __name__ == "__main__":
    print(reconcile(["order-1", "order-2"], ["order-1"]))
