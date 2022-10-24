#!/usr/bin/python3
"""Module that implements MyList Class"""


class MyList(list):
    """MyList class extends lists to
    include print_sorted method
    """
    def __init__(self):
        """initialises the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))
