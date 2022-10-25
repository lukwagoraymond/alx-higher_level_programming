#!/usr/bin/python3
"""5-save_to_json_file.py"""
import json


def save_to_json_file(my_obj, filename):
    """Function Writes JSON Object to File Object
    Args:
        my_obj (object): JSON Object
        filename (str): File to write to
    Returns:
        File written to
    """
    with open(filename, mode='w', encoding='utf8') as f:
        json.dump(my_obj, f)
