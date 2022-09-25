#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(0, len(str)):
        if str[i] == n:
            str_copy = str[:n] + str[n + 1:]
        else:
            str_copy = str[:]
    return str_copy
