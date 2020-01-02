import unittest
import os
from lusidjam.refreshing_token import RefreshingToken

class TestRefreshToken(unittest.TestCase):

    def test_refreshing_token(self):

        # Basic test to check that the function returns a hypothetical access token string from a txt file

        token = RefreshingToken(access_token_location ="sample_token.txt")
        self.assertEqual(token, "TEST123TOKEN")

    def test_refreshing_token_none(self):

        token = RefreshingToken(access_token_location="bad_location.txt")
        self.assertEqual(token, None)

    def test_refreshing_token_env_none(self):

        if "BAD_ENV_VARIABLE_2019" not in os.environ:
            token = RefreshingToken(access_token_location=os.getenv("BAD_ENV_VARIABLE_2019", None))
            self.assertEqual(token, None)
        else:
            self.skipTest("The environmental variable already exists, so cannot be used in this test")


if __name__ == '__main__':
    unittest.main()
