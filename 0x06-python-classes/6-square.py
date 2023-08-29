#!/usr/bin/python3
"""A module for a square class"""


class Square:
    """A class that defines a square by its size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with optional size and position"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Return the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Return the position of the square"""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square"""
        if not isinstance(position, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if any(not isinstance(n, int) or n < 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area"""
        return self.size ** 2

    def my_print(self):
        """Print the square with the character #"""
        if self.size == 0:
            print()
            return
        for i in range(self.position[1]):
            print()
        for i in range(self.size):
            print(" " * self.position[0] + "#" * self.size)
