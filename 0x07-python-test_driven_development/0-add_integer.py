#!/usr/bin/python3
"""
Module contains a function that adds 2 integers
"""


def add_integer(a, b=98):
    """Adds 2 integers """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        a = int(b)
    return a + b
