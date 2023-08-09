#!/usr/bin/python3
i = 122
upper = False

while i >= 97:
    if upper:
        print("{}".format(chr(i - 32)), end="")
        upper = False
    else:
        print("{}".format(chr(i)), end="")
        upper = True
    i -= 1
