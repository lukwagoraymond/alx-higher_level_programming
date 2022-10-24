#!usr/bin/python3
"""Square Class Definition"""


class Square:
    """Represents a Square
    Attributes:
        __size (int): size of side of a square
    """
    def __init__(self, size):
        """Creates an object of attribute size
        Args:
            size (int): Length or Width of Square
        Returns: None
        """
        self.__size = size
