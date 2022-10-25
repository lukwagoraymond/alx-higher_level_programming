#!/usr/bin/python3
"""4-from_json_string.py Module"""
import json


def from_json_string(my_str):
    """Function to load JSON data from str
        Args:
            my_str (str)
        Returns:
            Datastructure object
        """
    return json.loads(my_str)
