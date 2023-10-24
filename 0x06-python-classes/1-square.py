#!/usr/bin/python3
class Square:
    """
    This class defines a square

    Attributes:
        __size (int): This is the size f the square
    """
    def __init__(self, size=0):
        """
        Constructs a square with the given size

        Args:
            size (int): the size of the square. Default of 0 if not provided
        """
        self.__size = size
