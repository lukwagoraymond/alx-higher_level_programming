#!/usr/bin/python3
import sys

stderr_fileno = sys.stderr

text_input = ['and that piece of art is useful - Dora Korpar, 2015-10-19\n']

for i in text_input:
    if i != '':
        stderr_fileno.write(i)
exit(1)
