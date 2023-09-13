#!/usr/bin/python3
"""
A module containing a function to wrtie to a file
"""


def write_file(filename="", text=""):
    """
    Writes `text` to `filename`
    """

    with open(filename, "w", encoding='utf-8') as f:
        return (f.write(text))
