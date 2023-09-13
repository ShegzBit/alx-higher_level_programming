#!/usr/bin/python3
"""
A module containing a function that converts a a JSON rep
of a object(string)
"""
from json import dumps


def to_json_string(my_obj):
    """
    Returns the JSON rep of `my_obj`
    """
    return (dumps(my_obj))
