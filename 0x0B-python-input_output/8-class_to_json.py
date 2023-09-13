#!/usr/bin/python3
"""
Contains a function that serializes non basic types into their serializeables
"""


def class_to_json(obj):
    """
    Serializes the object obj
    """
    return (obj.__dict__)
