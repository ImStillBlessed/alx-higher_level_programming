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
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This function returns the dict representstion of an obj.
        """
        json_dict = {
            'first_name' = self.first_name,
            'last_name' = self.last_name,
            'age' = self.age
        }
        return json_dict
