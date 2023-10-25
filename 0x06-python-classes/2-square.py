"""
Author: Oigbochie Blessed
Task 2.
"""
#!/usr/bin/python3
class Square:
    """
    This is a vlass of a square with size

    Attributes:
        __size (int): this is the size of the square.
    """
    def __init__(self, size=0):
        """
        Constructs a square with a given size
        Args:
            size (int): The size of the square.
                Default is 0 if not provided.
        Raises:
            TypeError: If the size given is not a number
            ValueError: If the value is less than 0.
        """

