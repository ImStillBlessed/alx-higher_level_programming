#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


import json
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        """
        Returns a list of json string in dictiknary format
        """
        if not json_string or json_string is None:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        returns an instance with all attrinbutes already set
        """
        dummy_instance = cls(1, 1)
        dummy_instance.update(**dictionary)
        return dummy_instance

    @classmethod
    def load_from_file(cls):
        """
        Returns a list of Instances
        """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                dictionaries = json.load(file)
                return [cls.create(**d) for d in dictionaries]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to CSV and writes it to a file."""
        filename = cls.__name__ + ".csv"
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary().values())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes CSV file and returns a list of instances."""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                return [cls.create(**{k: int(v) for k, v in zip(cls.attributes, row)}) for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Opens a window and draws all the Rectangles and Squares."""
        turtle.speed(2)  # Adjust the speed as needed

        for rect in list_rectangles:
            turtle.penup()
            turtle.goto(rect.x, rect.y)
            turtle.pendown()
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)
            turtle.forward(rect.width)
            turtle.left(90)
            turtle.forward(rect.height)
            turtle.left(90)

        for square in list_squares:
            turtle.penup()
            turtle.goto(square.x, square.y)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(square.size)
                turtle.left(90)

        turtle.done()
