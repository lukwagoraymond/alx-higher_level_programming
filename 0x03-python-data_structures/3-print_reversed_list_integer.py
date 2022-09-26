#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Prints all items in a list in reverse order"""
    if my_list:
        for i in my_list[len(my_list) - 1::-1]:
            print('{:d}'.format(i))
