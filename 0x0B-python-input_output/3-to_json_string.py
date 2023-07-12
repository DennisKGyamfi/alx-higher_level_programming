#!/usr/bin/python3
"""
This module contains the to_json_string function
"""

import json


def to_json_string(my_obj):
    """ This function returns the jSON
    representation of an object(string)"""
    return (json.dumps(my_obj))
