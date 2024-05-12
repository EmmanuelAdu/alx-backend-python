#!/usr/bin/env python3
'''
A module for testing the utils module
'''


import unittest
from typing import Dict, Union, Tuple
from parameterized import parameterized

from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''
    Test cases for accessing values from nested maps
    '''

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ({"a": {"b": {"c": 3}}}, ("a", "b", "c"), 3),
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
    ) -> None:
        '''Tests `access_nested_map`'s output'''
        self.assertEqual(access_nested_map(nested_map, path), expected)
