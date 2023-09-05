#!/usr/bin/python3
class LockedClass:
    def __setattr__(self, name, value):
        if name not in ["first_name"]:
            raise AttributeError("object has no attribute 'last_name'")
        else:
            super().__setattr__(name, value)


if __name__ == "__main__":
    lc = LockedClass()
    lc.first_name = "John"
    try:
        lc.last_name = "Snow"
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
