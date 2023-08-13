#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    temp = my_list[0]
    for i in my_list:
        if i > temp:
            temp = i
    return temp


if __name__ == "__main__":
    my_list = None
    max_value = max_integer(my_list)
    print("Max: {}".format(max_value))
