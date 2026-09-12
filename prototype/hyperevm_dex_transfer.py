"""HyperEVM : contrôle d un transfert inter-DEX."""
import unittest
def net_amount(amount,fee): return amount-fee if amount>=fee else None
class Tests(unittest.TestCase):
 def test_transfer_after_fee(self): self.assertEqual(net_amount(100,2),98)
 def test_fee_exceeds_amount(self): self.assertIsNone(net_amount(1,2))
if __name__=="__main__": unittest.main()
