#!/usr/bin/python3
i = 0
while i <= 99:
    print('{:d}{:d}'.format(i // 10, i % 10), end=", ")
    i += 1
