import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from scanner import Scanner

class ScannerTest(unittest.TestCase):
    def setUp(self) -> None:
        self.s1 = Scanner()

    def test_scan_for_secrets(self):
        # Test 1: Password #TODO no rule for passwords yet
        # test_password = [
        #     "print('hello world')",
        #     "x = 1 + 1",
        #     "password = 'hunter2'",  # Should match
        #     "# this is a comment",
        #     "url = 'https://example.com?q=password'",  # Should NOT match (false positive test)
        #     "normal_string = 'this is just a string'"
        # ]

        # self.assertEqual(self.s1._scan_for_secrets(test_password), False)


        # Test 2: Generic API Key
        test_generic_api = [
            "api_endpoint = 'https://api.example.com'",
            "api_key = 'sk_live_1234567890abcdefghij'",  # Should match (30 chars)
            "license_key = 'ABC-123-DEF-456'",  # Should NOT match (too short)
            "token = 'abc123'",  # Should NOT match
            "normal_code = 'some_function_call()'",
            "another_key = 'short'",  # Should NOT match
        ]
        result = self.s1._scan_for_secrets(test_generic_api)
        self.assertIn(1, result) # only key should be 1 (for index where api key found)
        self.assertEqual(len(result), 1) # only should be one hit
        self.assertEqual(result[1], ('Generic API Key', "api_key = 'sk_live_1234567890abcdefghij'"))


        # Test 3: AWS Access Key ID
        test_aws_access = [
            "aws_region = 'us-east-1'",
            "aws_access_key = 'AKIAIOSFODNN7EXAMPLE'",  # Should match
            "fake_aws_key = 'AKIA1234567890ABCDE'",  # Should match (valid format)
            "not_a_key = 'AKIA-1234-5678-90AB'",  # Should NOT match (has dashes)
            "random_string = 'AKIAhelloworld12345'",  # Should NOT match (has lowercase)
            "some_id = '12345678901234567890'"  # Should NOT match (no AKIA prefix)
        ]

        result = self.s1._scan_for_secrets(test_aws_access)
        self.assertIn(1, result) # only key should be 1 (for index where api key found)
        self.assertEqual(len(result), 1) # only should be one hit
        self.assertEqual(result[1], ('AWS Access Key ID', "aws_access_key = 'AKIAIOSFODNN7EXAMPLE'"))
        # TODO Fix code so this test passes
        # Test 4: AWS Secret Access Key
        test_aws_secret = [
            "db_password = 'mypass123'",
            "aws_secret_key = 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'",  # Should match (40 chars)
            "short_secret = 'abc123'",  # Should NOT match
            "long_but_wrong = 'ThisIsAVeryLongStringButNotASecretKey123!'",  # Should NOT match (has symbols)
            "base64_data = 'dGVzdGluZzEyMzQ1Njc4OTA='",  # Should NOT match (32 chars, not 40)
            "another_string = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdef'",  # Should match (40 alphanumeric chars)
        ]

        # Test 5: No secrets at all (should return empty dict)
        test_no_secrets = [
            "print('Hello World')",
            "x = 42",
            "name = 'John Doe'",
            "url = 'https://example.com'",
            "comment = '# TODO: fix this later'",
            "data = [1, 2, 3, 4, 5]"
        ]




if __name__ == "__main__":
    unittest.main()
