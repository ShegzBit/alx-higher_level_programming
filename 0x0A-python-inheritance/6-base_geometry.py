#!/usr/bin/python3
"""Geometry class"""


class BaseGeometry:
    """Empty Geometry class"""

    def area(self):
        """Area Exeception"""
        raise Exception("area() is not implemented")


if __name__ == "__main__":
    bg = BaseGeometry()

    try:
        print(bg.area())
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
