#!usr/bin/python3
def remove_char_at(str, n):
    for i in range(0, len(str)):
        if str[i] == n:
            continue
        else:
            str_copy = str[:]
    return (str_copy)
