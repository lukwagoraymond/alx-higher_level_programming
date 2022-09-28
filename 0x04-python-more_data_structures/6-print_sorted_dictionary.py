#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_ol = sorted(list(a_dictionary))
    for i in sorted_ol:
        print("{:s}: {}".format(i, a_dictionary[i]))
