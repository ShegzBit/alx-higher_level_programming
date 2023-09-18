#!/usr/bin/python3
import unittest
from models.base import Base
from models.square import Square, Rectangle
import json
from io import StringIO


class ModTestCase(unittest.TestCase):
    """
    Modified test case
    """
    def assertWrite(self, filename, expected):
        """
        Checks if a write operation was carried out correctly
        """
        with open(filename, 'r') as f:
            output = f.read()
        self.assertEqual(output, expected)


class TestBase(ModTestCase):
    """A simple TestBase class definition
    """
    def test_0_first_instance_id(self):
        """tests id value
        """
        b_1 = Base()
        self.assertEqual(b_1.id, 1)

        b_2 = Base(12)
        self.assertEqual(b_2.id, 12)

        b_3 = Base()
        self.assertEqual(b_3.id, 2)

        b_4 = Base(None)
        self.assertEqual(b_4.id, 3)

        b_5 = Base(-3)
        self.assertEqual(b_5.id, -3)

        b_6 = Base(0)
        self.assertEqual(b_6.id, 0)

    def test_1_to_json_string(self):
        """
        Tests for Base class to_json_string static method
        """
        _list = [1, 1, 2, 3]
        self.assertEqual(Base.to_json_string(_list), '[1, 1, 2, 3]')

        r1 = Rectangle(1, 2)
        _dict = r1.to_dictionary()
        _output = json.dumps([_dict])
        self.assertEqual(Base.to_json_string([_dict]), _output)

        self.assertEqual(Base.to_json_string(None), '[]')

        self.assertEqual(Base.to_json_string([]), '[]')

        s1 = Square(1)
        _dict = s1.to_dictionary()
        _output = json.dumps([_dict])
        self.assertEqual(Base.to_json_string([_dict]), _output)

    def test_2_invalid_no_args(self):
        """
        Test for exception handling for invalid number of arguments
        """
        with self.assertRaises(TypeError):
            b1 = Base(2, 3, 4)
        with self.assertRaises(TypeError):
            b1 = Base(1, 2)

        with self.assertRaises(TypeError):
            Base.to_json_string()
        with self.assertRaises(TypeError):
            Base.to_json_string([], [], [])

    def test_3_save_to_file(self):
        """
        Test for save to file functionality
        """
        Rectangle.save_to_file(None)
        self.assertWrite("Rectangle.json", "[]")

        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])
    # Test for task 16, 17, 18


if __name__ == "__main__":
    unittest.main()
