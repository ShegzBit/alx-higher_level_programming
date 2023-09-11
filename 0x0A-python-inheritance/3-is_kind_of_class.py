#!/usr/bin/python3
"""A module for checking instance"""


def is_kind_of_class(obj, a_class):
    """checks if obj is an instance of a_class"""
    if isinstance(obj, a_class):
        return True
    return False


if __name__ == "__main__":
    a = 1
    if is_kind_of_class(a, int):
        print("{} comes from {}".format(a, int.__name__))
    if is_kind_of_class(a, float):
        print("{} comes from {}".format(a, float.__name__))
    if is_kind_of_class(a, object):
        print("{} comes from {}".format(a, object.__name__))
