#!/usr/bin/python3
"""Module for rebel python int class"""


class MyInt(int):
    """Rebel int"""
    def __eq__(self, other):
        """Rebel =="""
        return super().__ne__(other)

    def __ne__(self, other):
        """Rebel !="""
        return super().__eq__(other)


if __name__ == "__main__":
    my_i = MyInt(3)
    print(my_i)
    print(my_i == 3)
    print(my_i != 3)
