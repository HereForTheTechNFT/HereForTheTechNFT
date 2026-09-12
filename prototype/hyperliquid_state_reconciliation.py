"""Hyperliquid : comparer un état attendu et un état observé."""
import unittest
def reconcile(expected,observed): return sorted(set(expected)^set(observed))
class Tests(unittest.TestCase):
 def test_equal_states(self): self.assertEqual(reconcile(["a","b"],["b","a"]),[])
 def test_missing_event_is_reported(self): self.assertEqual(reconcile(["a","b"],["a"]),["b"])
if __name__=="__main__": unittest.main()
