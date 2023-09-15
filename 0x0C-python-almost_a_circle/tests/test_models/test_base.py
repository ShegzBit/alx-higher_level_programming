#!/usr/bin/python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """A simple TestBase class definition
    """
    def test_first_instance_id(self):
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
