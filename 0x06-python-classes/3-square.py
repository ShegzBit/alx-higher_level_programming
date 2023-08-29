#!/usr/bin/python3
"""
A Square class module that sets a private field size
and has a method area that uses the size to generate
and return the area
"""


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
        """Get the area of a sqaure"""
        return self.__size ** 2


if __name__ == "__main__":
    my_square_1 = Square(3)
    print("Area: {}".format(my_square_1.area()))

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    my_square_2 = Square(5)
    print("Area: {}".format(my_square_2.area()))
