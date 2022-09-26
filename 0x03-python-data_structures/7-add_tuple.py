#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Adds two Tuples of the same index"""
    if len(tuple_a) >= 2:
        cpy_tuple_a = tuple_a[:2]
    elif len(tuple_a) == 1:
        cpy_tuple_a = tuple_a[0], 0
    else:
        cpy_tuple_a = 0, 0

    if len(tuple_b) >= 2:
        cpy_tuple_b = tuple_b[:2]
    elif len(tuple_b) == 1:
        cpy_tuple_b = tuple_b[0], 0
    else:
        cpy_tuple_b = 0, 0

    return (cpy_tuple_a[0] + cpy_tuple_b[0], cpy_tuple_a[1] + cpy_tuple_b[1])
