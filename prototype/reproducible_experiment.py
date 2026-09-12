"""Mini-prototype de reproductibilité pour une expérience cryptographique."""
import hashlib
import unittest

def experiment_id(source, revision, inputs):
    payload='|'.join([source,revision,','.join(map(str,inputs))])
    return hashlib.sha256(payload.encode()).hexdigest()

def reproducible(a,b): return a==b

class ReproTests(unittest.TestCase):
    def test_same_inputs_same_id(self): self.assertTrue(reproducible(experiment_id('stark','main',[1,2]),experiment_id('stark','main',[1,2])))
    def test_revision_is_part_of_identity(self): self.assertNotEqual(experiment_id('stark','main',[1]),experiment_id('stark','v2',[1]))
    def test_input_change_is_detected(self): self.assertNotEqual(experiment_id('stark','main',[1]),experiment_id('stark','main',[2]))

if __name__ == "__main__": unittest.main()
