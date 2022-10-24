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
        self.size = size

    @property
    def size(self):
        """getter of __size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size
        Args:
            value (int): the size of the square
        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """Calculates Area of Square
        Args:

        Returns:
            square of Square
        """
        return self.__size ** 2
