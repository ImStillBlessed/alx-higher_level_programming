#!/usr/bin/python3
"""
Author: Oigbochie Blessed
Task 2.
"""
class Square:
    """
    This is a class of a square with size

    Attributes:
        __size (int): this is the size of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Constructs a square with a given size and position.

        Args:
            size (int): The size of the square.
                Default is 0 if not provided.
            position (tuple): marks the position of the square.
        Raises:
            TypeError: If the size given is not a number, or position
                is not a tuple of positive integers.
            ValueError: If the value is less than 0 in either size or
		position.
        """
        self.size = size
        self.position = position

    def my_print(self):
        """
        This method prints the square using #
        """
        i = 0
        while i < self.__size:
            j = 0
            while j < self.__size:
                print("#", end="")
                j += 1
            print("")
            i += 1
        if self.__size == 0:
            print("")
    @property
    def size(self):
        """
        This method retrives the value of the size attribute

        Returns:
            int: the value of the __size attribute.
        """
        return self.__size

    def area(self):
        """
        This method calc the current square area using size

        Returns: The square area
        """
        return (self._Square__size ** 2)
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError("size must be an integer")
        if value < 0:
             raise TypeError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        This method retrives the value of the size attribute

        Returns:
            int: the value of the __size attribute.
        """
        return self.__position
    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        if not all(isinstance(v, int) and v >= 0 for v in value):
            raise TypeError("position must be a tuple of 2 positive integer")
        self.__position = value
