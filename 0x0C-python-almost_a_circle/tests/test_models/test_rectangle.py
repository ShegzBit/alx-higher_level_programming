#!/usr/bin/python3
"""
A unittest for my rectangle class
"""
import unittest as unt
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle(unt.TestCase):
    """
    Test suites for Rectangle class
    """
    def test_1_super_call(self):
        """
        Test call to super class
        """
        b_1 = Base()
        self.assertEqual(b_1.id, 8)

        r_1 = Rectangle(10, 7)
        self.assertEqual(r_1.id, 9)

        r_2 = Rectangle(10, 10, 0, 0, 13)
        self.assertEqual(r_2.id, 13)

    def test_2_height_setter(self):
        """
        Test call to height setter
        """
        b_1 = Base()
        with self.assertRaises(AttributeError):
            print(b_1.height)

        r_1 = Rectangle(10, 7)
        self.assertEqual(r_1.height, 7)

        r_2 = Rectangle(10, 10, 0, 0, 13)
        self.assertEqual(r_2.height, 10)

        r_3 = Rectangle(10, 3)
        self.assertEqual(r_3.height, 3)

        r_4 = Rectangle(10, 10)
        self.assertEqual(r_4.height, 10)

        with self.assertRaises(TypeError):
            r_5 = Rectangle(10, "height")

    def test_3_width_setter(self):
        """
        Test for call to width setter
        """
        b_1 = Base()
        with self.assertRaises(AttributeError):
            print(b_1.width)

        r_1 = Rectangle(10, 7)
        self.assertEqual(r_1.width, 10)

        r_2 = Rectangle(2, 10, 0, 0, 13)
        self.assertEqual(r_2.width, 2)

        r_3 = Rectangle(10, 3)
        self.assertEqual(r_3.width, 10)

        with self.assertRaises(TypeError):
            r_4 = Rectangle("width", 10)

    def test_4_is_subclass(self):
        """
        Test for Rectangle is Base subclass
        """
        r_1 = Rectangle(10, 10)
        self.assertTrue(issubclass(type(r_1), Base))

    def test_5_x_y_setter(self):
        """
        Checks for call to x and y setters
        """
        # Test of base class error
        b_1 = Base()
        with self.assertRaises(AttributeError):
            print(b_1.x)
            print(b_1.y)

        # Main test of setter assignment
        r_1 = Rectangle(10, 10)
        self.assertTrue(r_1.x == 0 and r_1.y == 0)

        r_2 = Rectangle(10, 10, 2, 3, 10)
        self.assertTrue(r_2.x == 2 and r_2.y == 3)

        r_3 = Rectangle(10, 10, 100, 1000)
        self.assertTrue(r_3.x == 100 and r_3.y == 1000)

        with self.assertRaises(TypeError):
            r_4 = Rectangle(10, 10, "x", "y")

    def test_6_all_getters(self):
        """
        Tests all getter functions
        """
        r_1 = Rectangle(10, 10, 2, 10, 12)
        self.assertEqual(r_1.width, 10)
        self.assertEqual(r_1.height, 10)
        self.assertEqual(r_1.x, 2)
        self.assertEqual(r_1.y, 10)
        self.assertEqual(r_1.id, 12)

    def test_7_type_error(self):
        """
        Test for raise type exception when
        expected
        """
        r_0 = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r_1 = Rectangle("Width", 10)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r_2 = Rectangle(10, "Height")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r_3 = Rectangle(10, 12, "x")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r_4 = Rectangle(10, 12, 0, "y")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r_5 = Rectangle((1, 2, 3, 4), 12)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r_6 = Rectangle(1, [2, 4, 5])
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r_0.width = "12"
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r_0.height = (1, 2, 3, 4)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r_0.x = []
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r_0.y = {"x": 1, "y": 2}

    def test_8_value_error(self):
        """
        Test for raise value exception when
        expected
        """
        r_0 = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            # Width && Height
            # Test Exception against zero
            r_1 = Rectangle(0, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r_2 = Rectangle(10, 0)
            # Test Exception against -ve values
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r_3 = Rectangle(-2, 10)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r_4 = Rectangle(10, -2)

            # X && Y
            # Test against -ve number
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r_5 = Rectangle(1, 1, -2)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r_6 = Rectangle(1, 1, 0, -3)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r_0.width = 0
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r_0.width = -3
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r_0.height = -4
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r_0.height = 0
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r_0.x = -3
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r_0.y = -12

    def test_9_area(self):
        """
        Test for .area() output
        """
        r_1 = Rectangle(10, 10, 2, 10, 12)
        self.assertEqual(r_1.area(), 100)

        r_2 = Rectangle(2, 10, 0, 0, 13)
        self.assertEqual(r_2.area(), 20)

        r_3 = Rectangle(10, 7)
        self.assertEqual(r_3.area(), 70)

    def test_a__str__(self):
        """
        Test rectangle str
        """
        r_1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(str(r_1), '[Rectangle] (12) 2/1 - 4/6')

        r_2 = Rectangle(5, 5, 1, 0, 0)
        self.assertEqual(str(r_2), '[Rectangle] (0) 1/0 - 5/5')

        r_3 = Rectangle(1, 1, 0, 0, 0)
        self.assertEqual(str(r_3), '[Rectangle] (0) 0/0 - 1/1')

    def test_b_display(self):
        """
        Test rectangle ability to
        draw
        """
        from io import StringIO
        import sys

        def assertPrinted(self, r_display, result):
            """
            A custom assert function for checking
            and validating printed values or ouptut of operation
            in a function
            """
            io_main = StringIO()
            sys.stdout = io_main
            r_display()
            io_main = io_main.getvalue()
            sys.stdout = sys.__stdout__
            self.assertEqual(io_main, result)

        r_1 = Rectangle(1, 1)
        assertPrinted(self, r_1.display, "#\n")

        r_2 = Rectangle(10, 5)
        result = """\
##########
##########
##########
##########
##########
"""
        assertPrinted(self, r_2.display, result)

        r_3 = Rectangle(2, 8)
        result = """\
##
##
##
##
##
##
##
##
"""
        assertPrinted(self, r_3.display, result)

        r_4 = Rectangle(3, 5, 0, 0, 1)
        result = """\
###
###
###
###
###
"""
        assertPrinted(self, r_4.display, result)
        # Testing for compliance to x, y precision

        r_5 = Rectangle(3, 4, 1, 1)
        result = """\

 ###
 ###
 ###
 ###
"""
        assertPrinted(self, r_5.display, result)

        r_6 = Rectangle(1, 1, 1, 1)
        result = """\

 #
"""
        assertPrinted(self, r_6.display, result)

        r_7 = Rectangle(10, 10, 3, 4)
        result = """\




   ##########
   ##########
   ##########
   ##########
   ##########
   ##########
   ##########
   ##########
   ##########
   ##########
"""
        assertPrinted(self, r_7.display, result)

    def test_c_update_args(self):
        """
        Tests call to Rectangle.update
        """
        r_1 = Rectangle(10, 10, 2, 3, 4)
        self.assertEqual(r_1.id, 4)
        r_1.update(10)
        self.assertEqual(r_1.id, 10)
        r_1.update(10, 4, 3, 8, 0)
        self.assertEqual(r_1.width, 4)
        self.assertEqual(r_1.height, 3)
        self.assertEqual(r_1.x, 8)
        self.assertEqual(r_1.y, 0)
        r_1.update(5)
        self.assertEqual(r_1.id, 5)
        r_1.update(5, 19)
        self.assertEqual(r_1.width, 19)
        r_1.update(5, 19, 20)
        self.assertEqual(r_1.height, 20)
        r_1.update(5, 19, 20, 100)
        self.assertEqual(r_1.x, 100)
        r_1.update(5, 19, 20, 100, 8)
        self.assertEqual(r_1.y, 8)

        with self.assertRaises(ValueError):
            r_1.update(10, -2)

    def test_d_update_kwargs(self):
        """
        Test kwargs in update
        """
        r_1 = Rectangle(1, 1, 1, 1, 1)
        r_1.update(y=12, x=4)
        self.assertTrue(r_1.x == 4 and r_1.y == 12)
        r_1.update(1, 2, 3, width=10, id=10, height=12)
        self.assertTrue(r_1.width == 2 and r_1.height == 3 and r_1.id == 1)

    def test_e_invalid_argument(self):
        """
        Test for invalid number of argument
        """

        r_1 = Rectangle(1, 1, 1, 1, 1)
        r_1.update()
        self.assertTrue(r_1.id == 1 and r_1.width == 1 and r_1.height == 1)
        with self.assertRaises(TypeError):
            r_2 = Rectangle()
        with self.assertRaises(TypeError):
            r_2 = Rectangle(1)
        with self.assertRaises(TypeError):
            r_1.display("Square")
        with self.assertRaises(TypeError):
            r_1.display("Square", (1, 2))
        with self.assertRaises(TypeError):
            r_1.area(2)

    def test_f_to_dict(self):
        """
        Tests if Rectangle parses to dictionary appropraitely
        """
        r_1 = Rectangle(1, 1, 1, 1, 1)
        _dict = {"id": 1, "height": 1, "width": 1, "x": 1, "y": 1}
        self.assertEqual(r_1.to_dictionary(), _dict)

        r_2 = Rectangle(10, 2, 1, 9)
        _dict = {'x': 1, 'y': 9, 'id': 28, 'height': 2, 'width': 10}
        self.assertEqual(r_2.to_dictionary(), _dict)

        r_3 = Rectangle(1, 2)
        _dict = {'x': 0, 'y': 0, 'id': 29, 'height': 2, 'width': 1}
        self.assertEqual(r_3.to_dictionary(), _dict)
