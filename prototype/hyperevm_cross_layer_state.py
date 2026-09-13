#!/usr/bin/env python3
"""Toy state machine for HyperCore to HyperEVM transitions."""

from dataclasses import dataclass

@dataclass
class LayerState:
    core_height: int
    evm_height: int

def transition(state: LayerState, core_height: int, evm_height: int) -> LayerState:
    if core_height < state.core_height or evm_height < state.evm_height:
        raise ValueError("layer heights must be monotonic")
    if evm_height > core_height:
        raise ValueError("EVM state cannot outrun the observed core height")
    return LayerState(core_height, evm_height)

if __name__ == "__main__":
    print(transition(LayerState(10, 8), 11, 9))
