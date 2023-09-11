#!/usr/bin/python3
"""A module for sorted list class"""


class MyList(list):
    """Prints a list in sorted form"""

    def print_sorted(self):
        """Prints list in sorted form"""
        print(sorted(self))


if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)
    print(my_list)
    my_list.print_sorted()
    print(my_list)
