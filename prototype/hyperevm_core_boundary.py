"""HyperEVM : distinguer action EVM et confirmation HyperCore."""
import unittest
def core_confirmed(layer,finalized): return layer=="hypercore" and finalized
class Tests(unittest.TestCase):
 def test_evm_is_not_core_confirmation(self): self.assertFalse(core_confirmed("evm",True))
 def test_core_confirmation(self): self.assertTrue(core_confirmed("hypercore",True))
if __name__=="__main__": unittest.main()
