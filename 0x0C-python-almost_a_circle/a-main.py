#!/usr/bin/python3
""" 100-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    list_rectangles_input = [r1, r2]

    Rectangle.save_to_file_csv(list_rectangles_input)

    r1 = Square(10, 7, 2, 8)
    r2 = Square(2, 4)
    list_rectangles_input = [r1, r2]

    Square.save_to_file_csv(list_rectangles_input)

    Rectangle.load_from_file_csv()
    Square.load_from_file_csv()
