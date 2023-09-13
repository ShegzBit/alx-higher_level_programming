#!/usr/bin/python3
"""
My module for search and insert function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Appends new_string after search_string
    """
    with open(filename, "a+", encoding='utf-8') as f:
        i = 1
        for line in f:
            if search_string in line:
                print(f'found {search_string} on line {i}')
                i += 1
                break

append_after("0-read_file.py", 'l')
