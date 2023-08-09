#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
temp = number
if number < 0:
    number *= -1
while number >= 10:
    number %= 10

if temp < 0:
    number *= -1
if number == 0:
    write = f"Last digit of {temp:d} is {number:d} and is 0"
else:
    write = f"Last digit of {temp:d} is {number:d} and is greater than \
5" if number > 5 else f"Last digit of {temp:d} is \
{number:d} and is less than 6 and not 0"

print(write)
