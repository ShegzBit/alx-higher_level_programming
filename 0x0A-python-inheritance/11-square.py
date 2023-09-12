#!/usr/bin/python3
"""Geometry class"""


class BaseGeometry:
    """Empty Geometry class"""

    def area(self):
        """Area Exeception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value"""
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """A Rectangle subclass of BaseGeometry"""

    def __init__(self, width, height):
        """Constructor"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns area of rectangle self"""
        return self.__width * self.__height

    def __str__(self):
        """Informal string representation of rectangle"""
        return f'[Rectangle] {self.__width}/{self.__height}'


class Square(Rectangle):
    """A square subclass of rectangle"""
    def __init__(self, size):
        """Constructor"""
        Rectangle.integer_validator(self, "size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """Informal string representation of square"""
        return f'[Square] {self.__size}/{self.__size}'


if __name__ == "__main__":
    s = Square(13)

    print(s)
    print(s.area())
