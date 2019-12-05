import unittest
from lusidjam.refreshing_token import RefreshingToken

class TestRefreshToken(unittest.TestCase):

    def test_refreshing_token(self):

        # Basic test to check that the function returns a hypothetical access token string from a txt file

        token = RefreshingToken(access_token_location ="sample_token.txt")
        self.assertEqual(token, "TEST123TOKEN")

if __name__ == '__main__':
    unittest.main()
