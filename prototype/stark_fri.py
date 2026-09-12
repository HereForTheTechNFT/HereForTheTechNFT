"""Mini-prototype FRI : pliage et vérification de domaine."""
import unittest

def fri_fold(values, challenge, modulus):
    if not values or len(values)%2: raise ValueError('even domain required')
    half=len(values)//2
    return [(values[i]+challenge*values[i+half])%modulus for i in range(half)]

class FRITests(unittest.TestCase):
    def test_fold_reduces_domain(self): self.assertEqual(len(fri_fold([1,2,3,4],5,17)),2)
    def test_fold_is_deterministic(self): self.assertEqual(fri_fold([1,2],3,17),[7])
    def test_odd_domain_rejected(self):
        with self.assertRaises(ValueError): fri_fold([1,2,3],5,17)

if __name__ == "__main__": unittest.main()
