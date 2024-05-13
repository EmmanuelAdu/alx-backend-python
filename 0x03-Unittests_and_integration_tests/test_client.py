#!/usr/bin/env python3
'''A module for testing the client module'''


import unittest
from typing import Dict
from parameterized import parameterized
from unittest.mock import patch, MagicMock, PropertyMock


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

    def test_public_repos_url(self):
        '''Tests `public_repos_url`'''
        with patch(
                   "client.GithubOrgClient.org",
                   new_callable=PropertyMock
        ) as mock:
            mock.return_value = {
                "repos_url": "https://api.github.com/users/google/repos"
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
               "https://api.github.com/users/google/repos"
            )
