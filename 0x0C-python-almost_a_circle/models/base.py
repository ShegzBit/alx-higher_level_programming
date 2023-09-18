#!/usr/bin/python3
"""
Base Model class
"""
import json


class Base:
    """
    Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instance constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dict):
        if list_dict == [] or list_dict is None:
            return "[]"
        return json.dumps(list_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of list_objs to a file
        """
        write_list = '[]'
        list_dict = []
        if list_objs is None:
            write_list = '[]'
        else:
            for obj in list_objs:
                obj_dict = obj.to_dictionary()
                list_dict.append(obj_dict)
            write_list = Base.to_json_string(list_dict)
        filename = cls.__name__ + ".json"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(write_list)

    @staticmethod
    def from_json_string(json_string):
        """
        Converts json string to dictionary
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates an instance from a dictionary
        """
        from models.square import Rectangle, Square
        if cls.__name__ == "Rectangle":
            dummy = Rectangle(1, 1)
        elif cls.__name__ == "Square":
            dummy = Square(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load instances from file
        """
        from os import path
        filename = cls.__name__ + ".json"
        if not path.exists(filename):
            return []
        with open(filename, encoding='utf-8') as f:
            json_string_list = f.read()
        dict_list = Base.from_json_string(json_string_list)
        obj_list = []
        for _dict in dict_list:
            obj = cls.create(**_dict)
            obj_list.append(obj)
        return obj_list

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Uses python Turtle to draw shape
        """
        rect_size = len(list_rectangles)
        square_size = len(list_squares)

    def save_to_file_csv(cls, list_objs):
        """
        Serializes data to csv
        """
        name = cls.__name__
        filename = name + ".csv"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('[]')

        dict_list = []
        for obj in list_objs:
            _dict = obj.to_dictionary()
            dic_list.append(_dict)

    def load_from_file_csv(cls):
        """
        Loads from file
        """
        with open(filename, 'w', encoding='utf-8') as f:
            f.read()
