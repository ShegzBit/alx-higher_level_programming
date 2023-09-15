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
        self.assertEqual(b_1.id, 1)

        r_1 = Rectangle(10, 7)
        self.assertEqual(r_1.id, 2)

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
        with self.assertRaises(TypeError):
            r_1 = Rectangle("Width", 10)
            r_2 = Rectangle(10, "Height")
            r_3 = Rectangle(10, 12, "x")
            r_4 = Rectangle(10, 12, 0, "y")

    def test_8_value_error(self):
        """
        Test for raise value exception when
        expected
        """
        with self.assertRaises(ValueError):
            # Width && Height
            # Test Exception against zero
            r_1 = Rectangle(0, 10)
            r_2 = Rectangle(10, 0)
            # Test Exception against -ve values
            r_3 = Rectangle(-2, 10)
            r_4 = Rectangle(10, -2)

            # X && Y
            # Test against -ve number
            r_5 = Rectangle(1, 1, -2)
            r_6 = Rectangle(1, 1, 0, -3)

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


