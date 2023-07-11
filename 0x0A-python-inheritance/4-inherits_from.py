#!/usr/bin/python3
"""
this here module contains the inherits_from function
"""


def inherits_from(obj, a_class):

    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
