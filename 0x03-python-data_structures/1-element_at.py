#!/usr/bin/python3
def element_at(my_list, idx):
    """Retrives a value at a particular index"""
    if idx >= 0 and idx <= len(my_list) - 1:
        return my_list[idx]
