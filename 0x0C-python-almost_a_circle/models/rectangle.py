#!/usr/bin/python3
"""
Rectangle subclass of Base
"""
from models.base import Base


class Rectangle(Base):
    """
    Rectangle subclass of Base superclass
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """
        Width getter
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        Width setter
        """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        Height getter
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        Height setter
        """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        X getter
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        X setter
        """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        Y getter
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        Y setter
        """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """
        Calculates the area of the rectangle
        """
        return self.__height * self.__width

    def display(self):
        """
        Draws rectangle on screen
        """

        for i in range(self.__height):
            print(self.__width * '#')

    def __str__(self):
        """
        Informal string represention of Rectangle
        """
        _x = self.__x
        _y = self.__y
        _width = self.__width
        _height = self.__height
        return f'[Rectangle] ({self.id}) {_x}/{_y} - {_width}/{_height}'
