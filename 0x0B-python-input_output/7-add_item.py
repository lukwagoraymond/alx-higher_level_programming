#!/usr/bin/python3
"""Program to save strings from command line arguments to file called
`add_item.json`. File contains a json serialized list of all strings
entered as arguments to the program.
Example:
    $ ./7-add_item.py ALX School
    $ cat add_item.json ; echo ""
    ["Best", "School"]
    $ ./7-add_item.py Python 89 C
    $ cat add_item.json ; echo ""
    ["ALX", "Best", "School", "Python", "89", "C"]
"""
from sys import argv

if __name__ == "__main__":
    save_to_json_file = \
        __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    filename = "add_item.json"
    try:
        file_data = load_from_json_file(filename)
    except FileNotFoundError:
        file_data = []

    for arg in argv[1:]:
        file_data.append(arg)

    save_to_json_file(file_data, filename)
