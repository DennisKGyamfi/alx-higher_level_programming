#!/usr/bin/python3
"""
contains a function that returns True if the object
is exactly an instance of the specified class; otherwise False
"""


def is_same_class(obj, a_class):
    """returns true if obj is exactly an instance of a_class """
    return (type(obj) == a_class)
