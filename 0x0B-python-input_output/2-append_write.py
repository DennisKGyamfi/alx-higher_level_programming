#!/usr/bin/python3
"""
This module contains the append_write function
"""


def append_write(filename="", text=""):
    """ This function appends a string at
    the end of a text file(utf8) and returns the
    number of characters added
    """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
