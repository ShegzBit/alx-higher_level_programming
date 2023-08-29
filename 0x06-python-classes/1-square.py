#!/usr/bin/python3
"""A module for a square class with a constructor
That takes size and sets it as a private instance"""


class Square:
    """A Square class"""
    def __init__(self, size):
        """Square object constructor"""
        self.__size = size


if __name__ == "__main__":
    my_square = Square(3)
    print(type(my_square))
    print(my_square.__dict__)

    try:
        print(my_square.size)
    except Exception as e:
        print(e)

    try:
        print(my_square.__size)
    except Exception as e:
        print(e)
