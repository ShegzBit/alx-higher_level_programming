#!/usr/bin/python3

def reduce(func, my_list):
    result = 0
    for i in my_list:
        result = func(result, i)
    return result

def uniq_add(my_list=[]):
    result = reduce((lambda x, y: x + y), set(my_list))
    return result


if __name__ == "__main__":
    my_list = [1, 2, 3, 1, 4, 2, 5]
    result = uniq_add(my_list)
    print("Result: {:d}".format(result))
