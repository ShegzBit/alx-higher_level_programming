#!/usr/bin/python3
"""Module for locked class"""


class LockedClass:
    """Locked class"""
    def __setattr__(self, name, value):
        msg = "'LockedClass' object has no attribute 'last_name'"
        if name not in ["first_name"]:
            raise AttributeError(msg)
        else:
            super().__setattr__(name, value)
