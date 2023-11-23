#!/usr/bin/python3
"""
Module contains the `say_my_name` function
"""


def say_my_name(first_name, last_name=""):
    """Prints out <first_name> <last_name> """
    #   raising TypeError if either first or last names
    #   are not strings
    if type(first_name) not in [str]:
        raise TypeError('first_name must be a string')
    elif type(last_name) not in [str]:
        raise TypeError('last_name must be a string')
    else:
        #   returning formatted string if errors aren't raised
        print(f"My name is {first_name} {last_name}")
