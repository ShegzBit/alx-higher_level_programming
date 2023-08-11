#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    my_name = dir(hidden_4)
    for name in my_name:
        if name[0] != "_":
            print(name)
