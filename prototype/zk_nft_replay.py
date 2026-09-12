"""Mini-prototype ZK-NFT : liaison de contexte et anti-rejeu."""
import unittest

def proof_scope(contract, chain_id, token_id, nonce):
    return f"{contract}:{chain_id}:{token_id}:{nonce}"

def accepts(scope, used):
    return bool(scope) and scope not in used

class ScopeTests(unittest.TestCase):
    def test_scope_is_unique_to_context(self): self.assertNotEqual(proof_scope('nft',8453,7,1),proof_scope('nft',1,7,1))
    def test_first_use_is_accepted(self): self.assertTrue(accepts('nft:8453:7:1',set()))
    def test_replay_is_rejected(self): self.assertFalse(accepts('nft:8453:7:1',{'nft:8453:7:1'}))

if __name__ == "__main__": unittest.main()
