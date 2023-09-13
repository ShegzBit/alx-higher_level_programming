#!/usr/bin/python3
"""A module for a read file function"""


def read_file(filename=""):
    """Reads all data in a file"""
    with open(filename, "r",  encoding='utf-8') as f:
        file = f.read()
    print(file, end='')


if __name__ == "__main__":
    read_file("my_file_0.txt")
