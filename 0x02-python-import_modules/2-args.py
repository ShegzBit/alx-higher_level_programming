#!/usr/bin/python3
import sys

av = sys.argv[1:]
ac = len(av)
i = 1

if ac == 1:
    arg = "argument:"
elif ac == 0:
    arg = "arguments."
else:
    arg = "arguments:"

if __name__ == "__main__":
    print(f"{ac} {arg}")
    for a in av:
        print(f"{i}: {a}")
        i += 1
