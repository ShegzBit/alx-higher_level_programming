#!/usr/bin/python3
"""
A module contains a function that appends to a file
"""


def append_write(filename="", text=""):
    """
    Appends `text` to `filename`
    """
    with open(filename, "a", encoding='utf-8') as f:
        return (f.write(text))
