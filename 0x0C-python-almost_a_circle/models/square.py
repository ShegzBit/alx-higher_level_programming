#!/usr/bin/python3
"""
A module containing Square subclass of Rectangle
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        Instance constructor
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        Informal representation of Square
        in str
        """

        return f'[Square] ({self.id}) {self.x}/{self.y} - {self.width}'

    @property
    def size(self):
        """
        Size getter for Square instance
        """

        return self.width

    @size.setter
    def size(self, size):
        """
        Size setter for Square instance
        """
        self.width = size
        self.height = self.width

    def update(self, *args, **kwargs):
        """
        Updates the objects of the class
        """
        size = len(args)

        if size > 0:
            self.id = args[0]
        if size > 1:
            self.size = args[1]
        if size > 2:
            self.x = args[2]
        if size > 3:
            self.y = args[3]

        if size < 1:
            for key, arg in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, arg)

    def to_dictionary(self):
        """
        Parses all attributes of a class instance into a dictionary
        """
        _id = self.id
        _size = self.size
        _x = self.x
        _y = self.y
        return {"id": _id, "size": _size, "x": _x, "y": _y}
