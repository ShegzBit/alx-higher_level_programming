#!/usr/bin/python3

def to_upper(c):
    if islower(c):
        return chr(ord(c) - 32)
    return c


def islower(c):
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False


def uppercase(str):
    for c in str:
        print("{}".format(to_upper(c)), end="")
    print("{}".format("\n"), end="")
