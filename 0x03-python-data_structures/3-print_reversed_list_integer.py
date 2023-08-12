#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    rev_list = my_list[::-1]
    for x in rev_list:
        print("{:d}".format(x))


if __name__ == "__main__":
    my_list = []
    print_reversed_list_integer(my_list)
