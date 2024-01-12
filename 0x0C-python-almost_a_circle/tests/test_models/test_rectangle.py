#!/usr/bin/python3

"""Tests the rectangle module."""

from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    r1 = Rectangle(10, 2)
    r2 = Rectangle(2, 10)
    r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self) -> None:
        """Resets the values before the next test."""
        self.r1.width, self.r1.height = 10, 2
        self.r2.width, self.r2.height = 2, 10
        self.r3.width, self.r3.height = 10, 2

        # reset x values
        self.r1.x, self.r2.x, self.r3.x = 0, 0, 0

        # reset y values
        self.r1.y, self.r2.y, self.r3.y = 0, 0, 0

    def test_width_values(self):
        """Tests the width values of instantiated objects."""
        self.assertEqual(self.r1.width, 10)
        self.assertEqual(self.r2.width, 2)
        self.assertEqual(self.r3.width, 10)

    def test_width_updates(self):
        """Tests the modification of the object's width."""
        self.r1.width = 5
        self.r2.width = 7

        self.assertEqual(self.r1.width, 5)
        self.assertEqual(self.r2.width, 7)

    def test_height_values(self):
        """Tests the width values of instantiated objects."""
        self.assertEqual(self.r1.height, 2)
        self.assertEqual(self.r2.height, 10)
        self.assertEqual(self.r3.height, 2)

    def test_height_updates(self):
        """Tests the modification of the object's width."""
        self.r1.height = 5
        self.r2.height = 5

        self.assertEqual(self.r1.height, 5)
        self.assertEqual(self.r2.height, 5)

    def test_x_updates(self):
        """Tests the updates of a Rectangle object's `x` attribute."""
        self.r1.x = 5
        self.r2.x = 10
        self.r3.x = 15

        self.assertEqual(self.r1.x, 5)
        self.assertEqual(self.r2.x, 10)
        self.assertEqual(self.r3.x, 15)

    def test_y_updates(self):
        """Tests the updates of a Rectangle object's `y` attribute."""
        self.r1.y = 5
        self.r2.y = 10
        self.r3.y = 15

        self.assertEqual(self.r1.y, 5)
        self.assertEqual(self.r2.y, 10)
        self.assertEqual(self.r3.y, 15)

    def test_set_ids(self):
        """Tests objects that sets their own IDs."""
        self.assertEqual(self.r3.id, 12)

    def test_id_not_the_same(self):
        """Tests to ensure no two IDs are the same."""
        self.assertNotEqual(self.r1.id, self.r2.id)
        self.assertNotEqual(self.r3.id, self.r2.id)
        self.assertNotEqual(self.r1.id, self.r3.id)
