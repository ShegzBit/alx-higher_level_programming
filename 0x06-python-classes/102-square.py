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
        if not isinstance(size, int) and not isinstance(size, float):
            raise TypeError("size must be an number")
        elif size < 0:
            raise ValueError("size must be >= 0")
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
        if not isinstance(size, int) and not isinstance(size, float):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def __lt__(self, other):
        """Handles <"""
        return self.area() < other.area()

    def __eq__(self, other):
        """Handles =="""
        return self.area() == other.area()

    def __ne__(self, other):
        """Handles !="""
        return self.area() != other.area()

    def __gt__(self, other):
        """Handles >"""
        return self.area() > other.area()

    def __ge__(self, other):
        """Handle >="""
        return self.area() >= other.area()

    def __le__(self, other):
        """Hanlde <="""
        return self.area() <= other.area()


if __name__ == "__main__":
    s_5 = Square(5)
    s_6 = Square(6)

    if s_5 < s_6:
        print("Square 5 < Square 6")
    if s_5 <= s_6:
        print("Square 5 <= Square 6")
    if s_5 == s_6:
        print("Square 5 == Square 6")
    if s_5 != s_6:
        print("Square 5 != Square 6")
    if s_5 > s_6:
        print("Square 5 > Square 6")
    if s_5 >= s_6:
        print("Square 5 >= Square 6")
