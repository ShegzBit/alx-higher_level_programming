#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    mul_2 = []
    for i in my_list:
        mul_2.append(False) if i & 1 else mul_2.append(True)
    return mul_2
