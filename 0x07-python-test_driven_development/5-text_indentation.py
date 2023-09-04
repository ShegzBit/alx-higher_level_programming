#!/usr/bin/python3
"""A ALx module for TDD task 5"""


def text_indentation(text):
    """Prints text with indentation"""

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    prev = None
    for i in text:
        if i in ['.', '?', ':']:
            print(i, end='\n\n')
        elif i != ' ':
            print(i, end='')
        elif prev not in ['.', '?', ':'] and i == ' ':
            print(i, end='')
        prev = i
