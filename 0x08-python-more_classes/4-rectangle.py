#!/usr/bin/python3
"""A Module for python rectangle class"""


class Rectangle:
    """A Rectangle class"""
    def __init__(self, width=0, height=0):
        """Instance initializer"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the Area of Rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Return the Perimeter of Rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """Returns an unofficial string of an object"""
        my_square = []

        i = 0
        while i < self.__height:
            if i < self.__height - 1:
                my_square.append("#" * self.__width + "\n")
            else:
                my_square.append("#" * self.__width)
            i += 1
        return ''.join(my_square)

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"


if __name__ == "__main__":
    my_rectangle = Rectangle(2, 4)
    print(str(my_rectangle))
    print("--")
    print(my_rectangle)
    print("--")
    print(repr(my_rectangle))
    print("--")
    print(hex(id(my_rectangle)))
    print("--")

    # create new instance based on representation
    new_rectangle = eval(repr(my_rectangle))
    print(str(new_rectangle))
    print("--")
    print(new_rectangle)
    print("--")
    print(repr(new_rectangle))
    print("--")
    print(hex(id(new_rectangle)))
    print("--")

    print(new_rectangle is my_rectangle)
    print(type(new_rectangle) is type(my_rectangle))
