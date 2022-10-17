#!/usr/bin/python3
"""
    1-rectangle module
    Class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
"""


class Rectangle:
    """
        Class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
    """
    def __init__(self, width=0, height=0):
        """ Initialize instances"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ Set width"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Get width"""
        return self.__height

    @height.setter
    def height(self, value):
        """ Set width"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
