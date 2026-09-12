"""Base : reconciliation deterministe d un depot et retrait."""
import unittest
def reconcile(deposits,withdrawals): return sum(deposits)-sum(withdrawals)
class Tests(unittest.TestCase):
 def test_balanced_flow(self): self.assertEqual(reconcile([100,50],[80,70]),0)
 def test_unsettled_balance_is_visible(self): self.assertEqual(reconcile([100],[40]),60)
if __name__=="__main__": unittest.main()
