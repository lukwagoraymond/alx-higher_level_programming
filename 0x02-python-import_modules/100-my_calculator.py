#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div

    argz = sys.argv
    if len(argz) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if argz[2] != '+' and argz[2] != '-' and argz[2] != '*' and argz[2] != '/':
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(argz[1])
    b = int(argz[3])

    if argz[2] == '+':
        print("{} {} {} = {}".format(a, argz[2], b, add(a, b)))
    elif argz[2] == '-':
        print("{} {} {} = {}".format(a, argz[2], b, sub(a, b)))
    elif argz[2] == '*':
        print("{} {} {} = {}".format(a, argz[2], b, mul(a, b)))
    elif argz[2] == '/':
        print("{} {} {} = {}".format(a, argz[2], b, div(a, b)))
