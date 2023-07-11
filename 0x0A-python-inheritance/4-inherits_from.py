#!/usr/bin/python3
"""
this here module contains the inherits_from function
"""


def inherits_from(obj, a_class):
    """returns true if the object is an instance of a subclass """
    return(issubclass(type(obj), a_class) and type(obj) != a_class)
