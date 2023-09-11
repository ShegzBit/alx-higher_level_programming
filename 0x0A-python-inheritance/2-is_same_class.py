#!/usr/bin/python3
"""A module to check class"""


def is_same_class(obj, a_class):
    """Checks if a class is of type a_class"""
    if type(obj) is a_class:
        return True
    return False


if __name__ == "__main__":
    a = 1
    if is_same_class(a, int):
        print("{} is an instance of the class {}".format(a, int.__name__))
    if is_same_class(a, float):
        print("{} is an instance of the class {}".format(a, float.__name__))
    if is_same_class(a, object):
        print("{} is an instance of the class {}".format(a, object.__name__))
