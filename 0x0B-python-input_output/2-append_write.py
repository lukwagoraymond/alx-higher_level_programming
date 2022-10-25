#!/usr/bin/python3
"""2-append_write.py Module"""


def append_write(filename="", text=""):
    """Function to append string at end of file
    Args:
        filename (str): File to append to
        text (str): String to append to File
    Returns:
        number of characters written
    """
    with open(filename, mode='a', encoding='utf8') as f:
        return f.write(text)
