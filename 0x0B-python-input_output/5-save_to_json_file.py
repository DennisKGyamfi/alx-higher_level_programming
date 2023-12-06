#!/usr/bin/python3
"""
This module contains the save_to_json_file function
"""


import json


def save_to_json_file(my_obj, filename):
    """
    this function writess an object to a text file
    using a JSON representation
    """

    with open(filename, 'w') as f:
        json.dump(my_obj, f)
