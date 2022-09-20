#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        lstdig = number * -1
        number = lstdig % 10
    else:
        number = number % 10
    print("{}".format(number), end="")
    return number
