#!/usr/bin/python3
"""
A Square class module with a initializer/constructor that
takes a positive integer value and set it to a private
field size
"""


class Square:
    """A Square class"""
    def __init__(self, size=0):
        """Square constructor that takes a positive integer"""
        if type(size) is not (int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif size >= 0 and type(size) is (int):
            self.__size = size


if __name__ == "__main__":
    my_square_1 = Square(3)
    print(type(my_square_1))
    print(my_square_1.__dict__)

    my_square_2 = Square()
    print(type(my_square_2))
    print(my_square_2.__dict__)

    try:
        print(my_square_1.size)
    except Exception as e:
        print(e)

    try:
        print(my_square_1.__size)
    except Exception as e:
        print(e)

    try:
        my_square_3 = Square("3")
        print(type(my_square_3))
        print(my_square_3.__dict__)
    except Exception as e:
        print(e)

    try:
        my_square_4 = Square(-89)
        print(type(my_square_4))
        print(my_square_4.__dict__)
    except Exception as e:
        print(e)
