"""Hyperliquid : validation de nonce pour signatures."""
import unittest
def accept_nonce(nonce,last): return isinstance(nonce,int) and nonce>last
class Tests(unittest.TestCase):
 def test_increasing_nonce(self): self.assertTrue(accept_nonce(11,10))
 def test_reused_nonce(self): self.assertFalse(accept_nonce(10,10))
if __name__=="__main__": unittest.main()
