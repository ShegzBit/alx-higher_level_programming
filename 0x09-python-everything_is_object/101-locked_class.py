#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name not in ["first_name"]:
            raise AttributeError("""'LockedClass' object \
has no attribute 'last_name'""")
        else:
            super().__setattr__(name, value)
