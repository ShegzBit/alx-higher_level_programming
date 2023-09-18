#!/usr/bin/python3
"""
A module for testing Square class behaviours
"""
from models.square import Square, Rectangle
from models.base import Base
import unittest


class ModTestCase(unittest.TestCase):
    """
    Test suites with an assert for printed statements
    """

    def assertPrint(self, print_func, result):
        """
        Checks if an expected result is printed
        """
        from io import StringIO
        import sys

        io = StringIO()
        sys.stdout = io
        print_func()
        sys.stdout = sys.__stdout__
        io = io.getvalue()
        self.assertEqual(io, result)

    def test_0_init(self):
        """
        Test call to super.init
        """

        s1 = Square(1, 1, 1)
        self.assertEqual(s1.width, 1)
        self.assertEqual(s1.height, 1)
        self.assertEqual(s1.x, 1)
        self.assertEqual(s1.y, 1)
        self.assertEqual(s1.id, 30)

        s2 = Square(1, 1, 0)
        self.assertEqual(s2.x, 1)
        self.assertEqual(s2.y, 0)
        self.assertEqual(s2.width, 1)
        self.assertEqual(s2.height, 1)
        self.assertEqual(s2.id, 31)

        s3 = Square(2, 3, 1, 10)
        self.assertEqual(s3.id, 10)

    def test_1_type_exception(self):
        """
        Tests for type exception handling
        """
        # Test for TypeError on width and height
        s1 = Square(1, 1, 1, 2)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s1 = Square(1.2, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s2 = Square("Width", 1, 0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s3 = Square([], 1, 0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s4 = Square({}, 1, 0)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s5 = Square((), 1, 0)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s6 = Square(1, 1.2, 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s7 = Square(1, "height", 1)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s8 = Square(1, [], 0)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s9 = Square(1, {}, 10)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.x = {}
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s1.x = 1.4
        # Test for TypeError in x and y

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s10 = Square(1, 2, "main")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s10 = Square(1, 2, 1.2)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s10 = Square(1, 2, (1, 2))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s1.y = {}

    def test_1_value_exception(self):
        """
        Tests value Exception
        """
        s1 = Square(1, 2, 2, 3)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1 = Square(-2, 2, 10)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = -2
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s1.size = 0

    def test_2__str__(self):
        """
        Tests returned str
        """
        s1 = Square(5)
        self.assertEqual(str(s1), "[Square] (32) 0/0 - 5")

        s2 = Square(2, 2)
        self.assertEqual(str(s2), "[Square] (33) 2/0 - 2")

        s3 = Square(3, 1, 3)
        self.assertEqual(str(s3), "[Square] (34) 1/3 - 3")

        s4 = Square(3, 1, 3, 1)
        self.assertEqual(str(s4), "[Square] (1) 1/3 - 3")

    def test_3_invalid_no_args(self):
        """
        Tests for invalid number of arguments to methods
        """
        s1 = Square(5)
        with self.assertRaises(TypeError):
            s1 = Square()
        with self.assertRaises(TypeError):
            s1 = Square(1, 2, 3, 4, 5)
        with self.assertRaises(TypeError):
            s1.area(1)
        with self.assertRaises(TypeError):
            s1.area(1, 2)
        with self.assertRaises(TypeError):
            s1.display("size")
        with self.assertRaises(TypeError):
            s1.display(1, 2)

    def test_4_display(self):
        """
        Checks the display func
        """
        s1 = Square(5)
        result = "#####\n#####\n#####\n#####\n#####\n"
        self.assertPrint(s1.display, result)

        s2 = Square(5, 1, 1)
        result = "\n #####\n #####\n #####\n #####\n #####\n"
        self.assertPrint(s2.display, result)

        s3 = Square(4, 2, 2)
        result = "\n\n  ####\n  ####\n  ####\n  ####\n"
        self.assertPrint(s3.display, result)

        s4 = Square(2, 1, 1)
        result = "\n ##\n ##\n"
        self.assertPrint(s4.display, result)

        s1 = Square(5, 0, 0)
        result = "#####\n#####\n#####\n#####\n#####\n"

    def test_5_area(self):
        """
        Tests Square area
        """
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(10, 1, 2, 1)
        self.assertEqual(s2.area(), 100)

        s3 = Square(1, 0, 0, 0)
        self.assertEqual(s3.area(), 1)

        s4 = Square(8)
        self.assertEqual(s4.area(), 64)

    def test_6_update(self):
        """
        Test behaviour of update method
        """

        s1 = Square(5)
        s2 = Square(5)
        self.assertEqual(s1.size, 5)
        self.assertEqual(s1.id, 43)

        s1.update(10)
        self.assertEqual(s1.id, 10)

        s1.update(1, 2, 3)
        self.assertTrue(s1.size == 2 and s1.x == 3 and s1.id == 1)

        s1.update(1, 2, 3, size=1, x=12, id=100)
        self.assertTrue(s1.size == 2 and s1.x == 3 and s1.id == 1)

        s1.update(1, 2, 3, size_self=1, xy=12, id_self=100)
        self.assertTrue(s1.size == 2 and s1.x == 3 and s1.id == 1)

        s1.update(size=7, id=89, y=1)
        self.assertTrue(s1.size == 7 and s1.id == 89 and s1.y == 1)

        # Test that only attributes of square is updated
        s2.update(1, 2, 3)
        s2.update(size=7, id=89, y=1)

        self.assertEqual(vars(s1), vars(s2))

    def test_7_issubclass(self):
        """
        Tests if Square is a subclass of Rectangle and Base
        """
        self.assertTrue(issubclass(Square, Rectangle))
        self.assertTrue(issubclass(Square, Base))

    def test_8_to_dict(self):
        """
        Tests if Rectangle parses to dictionary appropraitely
        """
        s1 = Square(1, 1, 1, 1)
        _dict = {"id": 1, "size": 1, "x": 1, "y": 1}
        self.assertEqual(s1.to_dictionary(), _dict)

        s2 = Square(10, 2, 1, 9)
        _dict = {'x': 2, 'y': 1, 'id': 9, 'size': 10}
        self.assertEqual(s2.to_dictionary(), _dict)

        s3 = Square(1, 2)
        _dict = {'x': 2, 'y': 0, 'id': 45, 'size': 1}
        self.assertEqual(s3.to_dictionary(), _dict)

    def test_9_all_setter_getters(self):
        """
        Tests functionality of all setters
        """
        s1 = Square(1)
        self.assertEqual(s1.x, 0)
        self.assertEqual(s1.y, 0)
        self.assertEqual(s1.size, 1)
        self.assertEqual(s1.id, 46)

        s1.size = 12
        self.assertEqual(s1.size, 12)
        s1.size = 1
        self.assertEqual(s1.size, 1)

        s1.x = 0
        self.assertEqual(s1.x, 0)
        s1.x = 15
        self.assertEqual(s1.x, 15)

        s1.y = 0
        self.assertEqual(s1.y, 0)
        s1.y = 100
        self.assertEqual(s1.y, 100)

        s1.id = "Id :)"
        self.assertEqual(s1.id, "Id :)")
