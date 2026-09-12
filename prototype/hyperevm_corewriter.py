"""HyperEVM : modèle minimal d une commande CoreWriter."""
import unittest
def valid_command(action,nonce): return bool(action) and isinstance(nonce,int) and nonce>=0
class Tests(unittest.TestCase):
 def test_command(self): self.assertTrue(valid_command("transfer",0))
 def test_empty_action(self): self.assertFalse(valid_command("",0))
if __name__=="__main__": unittest.main()
