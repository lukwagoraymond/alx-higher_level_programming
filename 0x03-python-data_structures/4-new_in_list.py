#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces a value in a list at a particular position"""
    cpy_my_list = my_list[:]
    if idx >= 0 and idx <= len(cpy_my_list) - 1:
        cpy_my_list[idx] = element
    return cpy_my_list
