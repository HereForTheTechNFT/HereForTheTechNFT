"""Hyperliquid : transitions explicites du cycle de vie d un ordre."""
import unittest
TRANS={"new":{"accepted","cancelled"},"accepted":{"filled","cancelled"},"filled":set(),"cancelled":set()}
def transition(old,new): return new in TRANS.get(old,set())
class Tests(unittest.TestCase):
 def test_accept_then_fill(self): self.assertTrue(transition("accepted","filled"))
 def test_filled_cannot_reopen(self): self.assertFalse(transition("filled","accepted"))
if __name__=="__main__": unittest.main()
