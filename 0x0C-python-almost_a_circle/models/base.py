#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


import json


class Base:
    """
    This is the base class for managing id
    Attributes:
        nb_object
        id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Class constructor
        Args:
            id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """outputs the json representation for the base"""
        if list_dictionaries is None or list_dictionaries == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        This functikn writes the my_obj to a file in json.
        Args:
            cls (str)
            list_objs (list)
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", encoding="UTF-8") as a_file:
            if list_objs is None:
                file.write("[]")
            else:
                dictionaries = [obj.to_dictionary() for obj in list_objs]
            a_file.write(cls.to_json_string(dictionaries))


