#!/usr/bin/python3
from sys import stderr


def safe_function(fct, *args):
    result = None
    try:
        result = fct(*args)
    except Exception as ex:
        print("Exception: {}".format(ex), file=stderr)
    return result


if __name__ == "__main__":
    def my_div(a, b):
        return a / b

    result = safe_function(my_div, 10, 2)
    print("result of my_div: {}".format(result))

    result = safe_function(my_div, 10, 0)
    print("result of my_div: {}".format(result))

    def print_list(my_list, len):
        i = 0
        while i < len:
            print(my_list[i])
            i += 1
        return len
    result = safe_function(print_list, [1, 2, 3, 4], 10)
    print("result of print_list: {}".format(result))
