#!/usr/bin/python3
def no_c(my_string):
    """Prints string out without either 'C' or 'c'"""
    new_str = ''
    for char in my_string:
        if char == 'c' and char == 'C':
            continue
        new_str += char
