#!/usr/bin/python3
"""1-write_file.py Module"""


def write_file(filename="", text=""):
    """Function writes string to text file
    Args:
        filename (str): Filename to write to
        text (str):     Text to write to filename
    Returns:
        number of characters written
    """
    with open(filename, mode='w', encoding='utf8') as f:
        return f.write(text)
