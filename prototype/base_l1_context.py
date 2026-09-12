"""Base : associer explicitement réseau L1 et L2."""
import unittest
def context(chain_id,l1_block,l2_block): return (chain_id,l1_block,l2_block)
def valid(c): return c[0]==8453 and c[1]>=0 and c[2]>=0
class Tests(unittest.TestCase):
 def test_valid(self): self.assertTrue(valid(context(8453,100,200)))
 def test_wrong_network(self): self.assertFalse(valid(context(1,100,200)))
if __name__=="__main__": unittest.main()
