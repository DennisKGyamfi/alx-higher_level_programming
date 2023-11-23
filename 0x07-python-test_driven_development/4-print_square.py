#!/usr/bin/python3
"""
Module contains the ``print_square`` function
"""


def print_square(size):
    """Prints a square"""
    if type(size) != int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    elif (type(size) is float) and (size < 0):
        raise TypeError('size must be an integer')
    else:
        for i in range(size):
            print('#' * size)
