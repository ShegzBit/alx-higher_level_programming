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
