#!/usr/bin/python3
"""
Module containing a function that reads from a file
and convert the JSON string back to python object
"""
from json import load


def load_from_json_file(filename):
    """
    Loads data from a json file into a python obj
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return (load(f))
