"""Base : garde anti-rejeu pour messages cross-chain."""
import unittest
def accept(message_id,used): return bool(message_id) and message_id not in used
class Tests(unittest.TestCase):
 def test_new_message(self): self.assertTrue(accept("m1",set()))
 def test_replay(self): self.assertFalse(accept("m1",{"m1"}))
if __name__=="__main__": unittest.main()
