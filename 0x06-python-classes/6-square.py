#!/usr/bin/python3
"""
A Square class module that sets a private field size
and has a method area that uses the size to generate
and return the area
"""


class Square:
    """A square Object that models the behaviour of a real square"""
    def __init__(self, size=0, position=(0, 0)):
        """Square constructor"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif size >= 0 and isinstance(size, int):
            self.__size = size

        self.__position = position

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

        print("\n" * self.__position[1], end="")
        while i < self.__size:
            print(" " * self.__position[0] + "#" * self.__size)
            i += 1
        if self.__size == 0:
            print("")

    @property
    def position(self):
        """Gets size property of position"""
        return self.__position

    @position.setter
    def position(self, position):
        """Set the position of the square"""
        if (not isinstance(position, tuple) or len(position) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(not isinstance(i, int) or (i < 0) for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position


if __name__ == "__main__":
    my_square_1 = Square(3)
    my_square_1.my_print()

    print("--")

    my_square_2 = Square(3, (1, 1))
    my_square_2.my_print()

    print("--")

    my_square_3 = Square(3, (3, 0))
    my_square_3.my_print()

    print("--")
