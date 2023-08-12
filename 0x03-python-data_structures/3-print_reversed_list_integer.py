#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 1
    while i <= len(my_list):
        print("{:d}".format(my_list[len(my_list) - i]))
        i += 1


if __name__ == "__main__":
    my_list = []
    print_reversed_list_integer(my_list)
