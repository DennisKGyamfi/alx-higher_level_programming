#!/usr/bin/python3
"""
module contains the load from json file function
"""


import json


def load_from_json_file(filename):
    """
    Function creates an object from a JSON file
    """

    with open(filename) as f:
        content = json.load(f)
    return content
