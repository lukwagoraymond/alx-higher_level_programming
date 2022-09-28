#!/usr/bin/python3
def uniq_add(my_list=[]):
    """Adds all unique integers in a list"""
    sum = 0
    set_convert = set(my_list)
    for i in set_convert:
        sum += i
    return sum
