#!/usr/bin/python3

def advanced_reduce(my_list):
    tuple_sum = 0
    dividend = 0
    for i in my_list:
        tuple_sum += (i[0] * i[1])
        dividend += i[1]
    return tuple_sum / dividend


def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    return advanced_reduce(my_list)
