#!/usr/bin/python3

class Square:
    """A square Object that models the behaviour of a real square"""
    def __init__(self, size=0):
        """Square constructor"""
        if type(size) is not (int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif size >= 0 and type(size) is (int):
            self.__size = size

    def area(self):
