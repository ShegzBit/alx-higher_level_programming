#!/usr/bin/python3
"""
A Student class module
"""


class Student:
    """
    Student class
    """
    def __init__(self, first_name, last_name, age):
        """
        Constructor
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns a dictionary representation of
        Student
        """
        my_dict = {}
        if attrs is None:
            my_dict = self.__dict__
        else:
            for key in attrs:
                if key in self.__dict__:
                    my_dict[key] = self.__dict__.get(key)
        return my_dict

    def reload_from_json(self, json):
        """
        Reloads data froma json into python object
        """
        for key, value in json.items():
            if type(key) is str:
                setattr(self, key, value)
