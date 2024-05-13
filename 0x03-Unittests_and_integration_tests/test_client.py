#!/usr/bin/env python3
'''A module for testing the client module'''


import unittest
from typing import Dict
from parameterized import parameterized
from unittest.mock import patch, MagicMock


from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''Test cases for `GithubOrgClient`'''

    @parameterized.expand([
        ("google", {"login": "google"}),
        ("abc", {"login": "abc"}),
    ])
    @patch("client.get_json")
    def test_org(
            self,
            org: str,
            expected: Dict,
            mocked_function: MagicMock
    ) -> None:
        '''Tests `org`'''
        mocked_function.return_value = MagicMock(return_value=expected)
        check_client = GithubOrgClient(org)
        self.assertEqual(check_client.org(), expected)
        mocked_function.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
        )
