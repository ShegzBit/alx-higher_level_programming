#!/usr/bin/python3
"""A Module for python rectangle class"""


class Rectangle:
    """A Rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Instance initializer"""
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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

        _ps = type(self).print_symbol
        if isinstance(_ps, list):
            _ps = "".join(list(map(str, _ps)))
        else:
            _ps = str(_ps)
        for i in range(self.__height):
            row = []
            for j in range(self.__width):
                row.append(_ps)
            my_square.append("".join(row))
        return "\n".join(my_square)

    def __repr__(self):
        """Returns an official str representation of an object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Object destructor"""
        print("Bye rectangle...")
        if type(self).number_of_instances > 0:
            type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Is bigger or is equal"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        r2 = rect_2.area()
        r1 = rect_1.area()
        if (r2 > r1):
            return rect_2
        return rect_1


my_rectangle_1 = Rectangle(8, 4)
my_rectangle_2 = Rectangle(2, 3)

if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")


my_rectangle_2.width = 10
my_rectangle_2.height = 5
if my_rectangle_1 is Rectangle.bigger_or_equal(my_rectangle_1, my_rectangle_2):
    print("my_rectangle_1 is bigger or equal to my_rectangle_2")
else:
    print("my_rectangle_2 is bigger than my_rectangle_1")
