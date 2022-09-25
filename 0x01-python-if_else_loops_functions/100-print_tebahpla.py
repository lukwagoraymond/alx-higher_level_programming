#!/usr/bin/python3
for char in range(122, 96, -2):
    print('{}{}'.format(chr(char), chr((char - 1) - 32)), end="")
