#!/usr/bin/python3

"""Tests the rectangle module."""

from ctypes.wintypes import HENHMETAFILE
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

    # Test for missing positional arguments

    def test_missing_positional_width_arg(self):
        """Tests for the missing width attribute when instantiating."""
        with self.assertRaises(TypeError) as no_width:
            Rectangle(height=2)

        self.assertEqual(
            no_width.exception.__str__(),
            "__init__() missing 1 required positional argument: 'width'",
        )

    def test_missing_positional_height_arg(self):
        """Tests for the missing height attribute when instantiating."""
        with self.assertRaises(TypeError) as no_height:
            Rectangle(width=10)

        self.assertEqual(
            no_height.exception.__str__(),
            "__init__() missing 1 required positional argument: 'height'",
        )

    def test_missing_positional_args(self):
        """
        Tests for the missing width and height attributes when instantiating.
        """
        with self.assertRaises(TypeError) as no_height_width:
            Rectangle()

        self.assertEqual(
            no_height_width.exception.__str__(),
            "__init__() missing 2 required positional arguments: "
            "'width' and 'height'",
        )

    # Test for expected behavior when the attributes are correctly set.

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

    # Test to ensure no two objects have the same ID

    def test_set_ids(self):
        """Tests objects that sets their own IDs."""
        self.assertEqual(self.r3.id, 12)

    def test_id_not_the_same(self):
        """Tests to ensure no two IDs are the same."""
        self.assertNotEqual(self.r1.id, self.r2.id)
        self.assertNotEqual(self.r3.id, self.r2.id)
        self.assertNotEqual(self.r1.id, self.r3.id)

    # Test for TypeError exceptions raised when setting the attributes.

    def test_invalid_type_for_width_set(self):
        """
        Tests for TypeError exceptions when setting or updating the `width`
        attribute.
        """
        with self.assertRaises(TypeError) as type_error:
            self.r1.width = 1.4
            self.r1.width = True
            self.r4.width = "five"

        # ensure the exception message is as expected
        self.assertEqual(
            type_error.exception.__str__(), "width must be an integer"
        )

    def test_invalid_type_for_height_set(self):
        """
        Tests for TypeError exceptions when setting or updating the `height`
        attribute.
        """
        with self.assertRaises(TypeError) as type_error:
            self.r1.height = 1.4
            self.r1.height = True
            self.r4.height = "five"

        # ensure the exception message is as expected
        self.assertEqual(
            type_error.exception.__str__(), "height must be an integer"
        )

    def test_invalid_type_for_x_set(self):
        """
        Tests for TypeError exceptions when setting or updating the `x`
        attribute.
        """
        with self.assertRaises(TypeError) as type_err:
            self.r1.x = 1.4
            self.r1.x = True
            self.r4.x = "five"

        # ensure the exception message is as expected
        self.assertEqual(type_err.exception.__str__(), "x must be an integer")

    def test_invalid_type_for_y_set(self):
        """
        Tests for TypeError exceptions when setting or updating the `y`
        attribute.
        """
        with self.assertRaises(TypeError) as type_err:
            self.r1.y = 1.4
            self.r1.y = True
            self.r4.y = "five"

        # ensure the exception message is as expected
        self.assertEqual(type_err.exception.__str__(), "y must be an integer")

    # Test for ValueError exceptions raised when setting the attributes.

    def test_invalid_value_for_width_set(self):
        """
        Tests for TypeError exceptions when setting or updating the `width`
        attribute.
        """
        with self.assertRaises(ValueError) as value_error:
            self.r1.width = -34
            self.r1.width = -1
            self.r4.width = 0

        # ensure the exception message is as expected
        self.assertEqual(value_error.exception.__str__(), "width must be > 0")

    def test_invalid_value_for_height_set(self):
        """
        Tests for ValueError exceptions when setting or updating the `height`
        attribute.
        """
        with self.assertRaises(ValueError) as value_error:
            self.r1.height = -34
            self.r1.height = -1
            self.r4.height = 0

        # ensure the exception message is as expected
        self.assertEqual(value_error.exception.__str__(), "height must be > 0")

    def test_invalid_value_for_x_set(self):
        """
        Tests for ValueError exceptions when setting or updating the `x`
        attribute.
        """
        with self.assertRaises(ValueError) as value_error:
            self.r1.x = 0
            self.r1.x = -1
            self.r4.x = -45

        # ensure the exception message is as expected
        self.assertEqual(value_error.exception.__str__(), "x must be >= 0")

    def test_invalid_value_for_y_set(self):
        """
        Tests for ValueError exceptions when setting or updating the `y`
        attribute.
        """
        with self.assertRaises(ValueError) as value_error:
            self.r1.y = 0
            self.r1.y = -1
            self.r4.y = -45

        # ensure the exception message is as expected
        self.assertEqual(value_error.exception.__str__(), "y must be >= 0")
