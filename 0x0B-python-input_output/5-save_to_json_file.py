#!/usr/bin/python3
"""
A module containing a function that dumps
the JSON rep of a python object into a file
"""
from json import dump


def save_to_json_file(my_obj, filename):
    """
    creates a json object from a python obj and stores
    it in filename
    """
    with open(filename, "w", encoding='utf-8') as f:
        dump(my_obj, f)
