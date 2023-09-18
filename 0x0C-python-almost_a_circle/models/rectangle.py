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

        if self.height > 0:
            print(self.y * "\n", end="")
        for i in range(self.__height):
            print(self.x * " " + self.__width * '#')

    def __str__(self):
        """
        Informal string represention of Rectangle
        """
        _x = self.__x
        _y = self.__y
        _width = self.__width
        _height = self.__height
        return f'[Rectangle] ({self.id}) {_x}/{_y} - {_width}/{_height}'

    def update(self, *args, **kwargs):
        """
        Updates the objects of the class
        """
        size = len(args)

        if size > 0:
            self.id = args[0]
        if size > 1:
            self.width = args[1]
        if size > 2:
            self.height = args[2]
        if size > 3:
            self.x = args[3]
        if size > 4:
            self.y = args[4]

        if size < 1:
            for key, arg in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, arg)

    def to_dictionary(self):
        """
        Parses the attributes of a class instance into a dictionary
        """
        _id = self.id
        width = self.width
        _height = self.height
        _x = self.x
        _y = self.y
        return {"id": _id, "width": width, "height": _height, "x": _x, "y": _y}
