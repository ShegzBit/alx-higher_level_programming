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

    def my_print(self):
        """Draws self.square on screen"""
        i = 0
        while i < self.__size:
            print("#" * self.__size)
            i += 1
        if self.__size == 0:
            print("")


if __name__ == "__main__":
    my_square = Square(3)
    my_square.my_print()

    print("--")

    my_square.size = 10
    my_square.my_print()

    print("--")

    my_square.size = 0
    my_square.my_print()

    print("--")
