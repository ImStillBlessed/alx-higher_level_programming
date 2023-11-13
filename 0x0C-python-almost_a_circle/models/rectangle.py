#!/usr/bin/python3
"""
Author:
    Oigbochie Blessed
"""


from models.base import Base


class Rectangle(Base):
    """the rectangle class inheriting from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        constructor for Rectangle
        Args:
            width
            height
            x
            y
            id
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        prints to stdout the rectangle
        """
        for _ in range(self.y):
            print()
        for _ in range(self.__height):
            print(" " * self.x + "#" * self.__width)

    def __str__(self):
        """
        Updates the __str__ function
        """
        row = self.__width
        col = self.__height
        return (f"[Rectangle] ({self.id}) {self.x}/{self.y} - {row}/{col}")

    @property
    def width(self):
        """returns the value property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the value of the width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """returns the value property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the value of the height
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """returns the value property x"""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Sets the value of the x
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """returns the value property y"""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Sets the value of the y
        """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__y = value

    def update(self, *args, **kwargs):
        """
        updates the arguments in order
        no-keyword arguments
        and key-worded-arguments
        """
        attributes = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i in range(len(args)):
                setattr(self, attributes[i], args[i])
        if kwargs:
            for key, value in kwargs.items():
                if key in attributes:
                    setattr(self, key, value)

    def to_dictionary(self):
        """Pastss the valuss of attribuyes in a dictionary
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
