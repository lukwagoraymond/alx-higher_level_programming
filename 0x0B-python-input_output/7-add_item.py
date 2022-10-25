#!/usr/bin/python3
""" 7-add_item.py
Program to save strings from command line arguments to file called
`add_item.json`. File contains a json serialized list of all strings
entered as arguments to the program.
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_item(args, filename):
    """
        adds items to a json file
        @args (objects): The arguments that need to be added.
        @filename: The file that needs to be updated
    """
    try:
        content = load_from_json_file(filename)
    except IOError:
        content = []

    for item in args:
        content.append(item)
    save_to_json_file(content, filename)


if __name__ == "__main__":
    args = sys.argv[1:]
    filename = "add_item.json"
    add_item(args, filename)
