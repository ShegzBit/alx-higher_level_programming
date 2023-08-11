#!/usr/bin/python3
import sys

av = sys.argv[1:]
ac = len(av)
i = 1

arg = "argument." if ac == 0 else "arguments:"

print(f"{ac} {arg}")
for a in av:
    print(f"{i}: {a}")
    i += 1
