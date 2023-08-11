#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
import sys

if __name__ == "__main__":
    av = sys.argv[1:]
    if len(av) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    x = int(av[0])
    y = int(av[2])
    match av[1]:
        case "+":
            result = add(x, y)
        case "-":
            result = sub(x, y)
        case "*":
            result = mul(x, y)
        case "/":
            result = div(x, y)
        case _:
            result = None
    if result is None:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    print("{} {} {} = {}".format(x, av[1], y, result))
