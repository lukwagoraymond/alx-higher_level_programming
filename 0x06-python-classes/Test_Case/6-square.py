#!usr/bin/python3
"""Square Class Definition"""


class Square:
    """Represents a Square
    Attributes:
        __size (int): size of side of a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Creates an object of attribute size
        Args:
            size (int): Length or Width of Square
        Returns: None
        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """getter for __position
        Returns:
            position of the square in 2D space
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position
        Args:
            value (tuple): the position of the square in 2D space
        Returns:
            None
        """
        if type(value) is not tuple or len(value) != 2 or \
           type(value[0]) is not int or value[0] < 0 or \
           type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates Area of Square
        Args:

        Returns:
            square of Square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square
        Returns:
            None
        """
        if self.__size != 0:
            for a in range(self.__position[1]):
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
        else:
            print()
