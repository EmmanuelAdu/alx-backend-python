#!/usr/bin/env python3
'''
A module for testing the utils module
'''


import unittest
from unittest.mock import patch, Mock
from typing import Dict, Union, Tuple
from parameterized import parameterized

from utils import (
    access_nested_map,
    get_json,
    memoize
)


class TestAccessNestedMap(unittest.TestCase):
    '''Test cases for accessing values from nested maps'''

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

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            exception: Exception,
    ):
        '''Tests `access_nested_map`'s exception'''
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    '''Test cases for `get_json`'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(
            self,
            test_url: str,
            test_payload: Dict
    ) -> None:
        '''Tests `get_json`'s output'''
        mock_data = {'json.return_value': test_payload}
        with patch("requests.get", return_value=Mock(**mock_data)) as mock_get:
            self.assertEqual(get_json(test_url), test_payload)
            mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    '''Test cases for `memoize`'''

    def test_memoize(self):
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, 'a_method', return_value=42) as mock:
            test = TestClass()
            self.assertEqual(test.a_property(), 42)
            self.assertEqual(test.a_property(), 42)
            mock.assert_called_once()
