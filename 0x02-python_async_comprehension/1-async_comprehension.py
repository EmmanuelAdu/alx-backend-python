#!/usr/bin/env python3
'''Async Comprehensions
'''
from typing import List
from importlib import import_module as using


async_generator = using('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Creates a list of 10 numbers from a 10-number generator
    '''
    return [n async for n in async_generator()]
