#!/usr/bin/python3
"""
A module containing a function that converts a JSON rep
to python object format
"""
from json import loads


def from_json_string(my_str):
    """
    convert `my_str` to a python object format
    """
    return (loads(my_str))
