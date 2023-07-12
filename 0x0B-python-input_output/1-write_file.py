#!/usr/bin/python3
""" this module contains the write_file function"""


def write_file(filename="", text=""):
    """ this fucntion writes a string to a text file(utf8)
    and returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        return (len(text))
