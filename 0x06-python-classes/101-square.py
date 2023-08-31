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
        self.size = size
        self.position = position

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
        self.__size = size

    def my_print(self):
        """Draws self.square on screen"""
        i = 0

        if self.__size > 0:
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

    def __str__(self):
        """Draws self.square on screen"""
        i = 0
        new_list = list()

        if self.__size > 0:
            new_list.append("\n" * self.__position[1])
        while i < self.__size:
            my_str = " " * self.__position[0] + "#" * self.__size + "\n"
            my_str2 = " " * self.__position[0] + "#" * self.__size
            (new_list.append(my_str) if i < self.__size - 1
                else new_list.append(my_str2))
            i += 1
        if self.__size == 0:
            new_list.append("\n")
        return "".join(new_list)
