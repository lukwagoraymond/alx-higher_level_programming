#!/usr/bin/env python3
"""7-add_item.py
Program to save strings from command line arguments to file called
`add_item.json`. File contains a json serialized list of all strings
entered as arguments to the program.
"""

import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    filename = "add_item.json"

    try:
        arg_list = load_from_json_file(filename)
    except IOError:
        arg_list = []

    for arg in sys.argv[1:]:
        arg_list.append(arg)
    save_to_json_file(arg_list, filename)
