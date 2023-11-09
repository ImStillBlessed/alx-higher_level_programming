#!/usr/bin/python3
"""
Author:
    Oigbochie Nlessed
"""


class Student():
    """
    This class defines a student.
    Attributes:
        first_name (str): the first name of the student
        last_name (str): the last name of the student.
        age (int): the age of the student.
    """
    def __init__(self, first_name, last_name, age):
        """
        Student objecr constructor
        first_name (str): must be a str.
        last_name : must be a str.
        age : must be an integer.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This function returns the dict representstion of an obj.
        Returns:
            the json dictionary representation of class Student.
        """
        if attrs is None:
            return {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age
            }
        else:
            json_dict = {}
            for attr in attrs:
                if hasattr(self, attr):
                    json_dict[attr] = getattr(self, attr)
            return json_dict

    def relaod_from_json(self, json):
        """
        Loads a dictionary from json and replaces the attributes of student
        with the key and values.
        Args:
            json: the dict to use.
        """
        for key, value in json.items():
            setattr(self, key, value)
