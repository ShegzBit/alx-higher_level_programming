#!/usr/bin/python3
"""Add attribute function module"""


def is_mutable(cls):
    """Checks if an object is mutable"""
    immutable_types = (int, float, bool, str, tuple, frozenset)
    return not isinstance(cls, immutable_types)


def add_attribute(cls, name, value):
    """Adds attribute name to cls"""
    if is_mutable(cls):
        cls.name = value
    else:
        raise TypeError("can't add new attribute")
