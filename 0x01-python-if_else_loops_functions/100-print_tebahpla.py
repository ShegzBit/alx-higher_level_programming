#!/usr/bin/python3
i = 122
upper = False

while i >= 97:
    if upper:
        print(chr(i - 32), end="")
        upper = False
    else:
        print(chr(i), end="")
        upper = True
    i -= 1
