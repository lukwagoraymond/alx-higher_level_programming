#!/usr/bin/python3
"""3-to_json_string.py Module"""
import json


def to_json_string(my_obj):
    """Function to convert JSON to string object
    Args:
        my_obj (object)
    Returns:
        String representation of JSON
    """
    return json.dumps(my_obj)
