#!/usr/bin/python3
"""Defines a Locked class"""


class LockedClass:
    """
    A Locked class that only lets the user dynamically create the instance
    attribute 'first_name'
    """

    __slots__ = ['first_name']
