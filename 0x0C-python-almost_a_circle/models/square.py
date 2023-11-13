#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This class defines a special rectangle
    a square
    no new attributes all inherited
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        initializes the square from the rectangle
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setted for size"""
        self.width = value
        self.height = value

    def __str__(self):
        """
        Overrides the __str__ method
        """
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        """
        updatss the attributes in order
        """
        attributes = ['id', 'size', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        if kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """returns the dictionary representaion of the square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
