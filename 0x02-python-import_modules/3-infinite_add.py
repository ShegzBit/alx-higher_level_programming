#!/usr/bin/python3
import sys

if __name__ == "__main__":
    av = sys.argv[1:]
    sum = 0

    for a in av:
        sum += int(a)
    print("{}".format(sum))
