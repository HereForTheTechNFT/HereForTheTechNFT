"""Mini-prototype STARK : trace et contraintes AIR."""
import unittest

def air_ok(trace, delta, modulus):
    return bool(trace) and all((b-a-delta)%modulus==0 for a,b in zip(trace,trace[1:]))

class AIRTests(unittest.TestCase):
    def test_valid_trace(self): self.assertTrue(air_ok([2,5,8],3,17))
    def test_invalid_transition(self): self.assertFalse(air_ok([2,6,8],3,17))
    def test_empty_trace(self): self.assertFalse(air_ok([],3,17))

if __name__ == "__main__": unittest.main()
