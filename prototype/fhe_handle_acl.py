"""Mini-prototype FHE : validation de handles et ACL."""
import unittest

def handle_valid(handle):
    return isinstance(handle,str) and handle.startswith('ct:') and len(handle)>3

def can_decrypt(handle, actor, acl):
    return handle_valid(handle) and actor in acl.get(handle,set())

class FHETests(unittest.TestCase):
    def test_valid_handle_with_acl(self): self.assertTrue(can_decrypt('ct:42','alice',{'ct:42':{'alice'}}))
    def test_unknown_actor_is_denied(self): self.assertFalse(can_decrypt('ct:42','bob',{'ct:42':{'alice'}}))
    def test_plaintext_is_not_a_handle(self): self.assertFalse(handle_valid('42'))

if __name__ == "__main__": unittest.main()
