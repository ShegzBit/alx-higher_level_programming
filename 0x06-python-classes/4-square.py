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
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif size >= 0 and isinstance(size, int):
            self.__size = size

    def area(self):
        """Get the area of a sqaure"""
        return self.__size ** 2

    @property
    def size(self):
        """Gets size property of square"""
        return self.__size

    @size.setter
    def size(self, size):
        """Sets size property of square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif size >= 0 and isinstance(size, int):
            self.__size = size


if __name__ == "__main__":
    my_square = Square(89)
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    my_square.size = 3
    print("Area: {} for size: {}".format(my_square.area(), my_square.size))

    try:
        my_square.size = "5 feet"
        print("Area: {} for size: {}".format(my_square.area(), my_square.size))
    except Exception as e:
        print(e)
