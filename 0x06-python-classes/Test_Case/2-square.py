#!usr/bin/python3
"""Square Class Definition"""


class Square:
    """Represents a Square
    Attributes:
        __size (int): size of side of a square
    """
    def __init__(self, size=0):
        """Creates an object of attribute size
        Args:
            size (int): Length or Width of Square
        Returns: None
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
