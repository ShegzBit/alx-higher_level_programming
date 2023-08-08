#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# YOUR CODE HERE
if number == 0:
    print("{} is zero".format(number))
    exit(0)
write = f"{number:d} is positive" if number >= 0 else f"{number:d} is negative"
print(write)
