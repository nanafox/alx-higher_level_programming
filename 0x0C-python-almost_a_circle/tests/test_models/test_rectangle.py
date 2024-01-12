#!/usr/bin/python3

"""Tests the rectangle module."""

from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Tests the Rectangle class of the rectangle module."""

    r1 = Rectangle(10, 2)
    r2 = Rectangle(2, 10)
    r3 = Rectangle(10, 2, 0, 0, 12)

    def tearDown(self) -> None:
        """Resets the values before the next test."""
        self.r1.update(id=1, width=10, height=2, x=0, y=0)
        self.r2.update(id=2, width=2, height=10, x=0, y=0)
        self.r3.update(id=12, width=10, height=2, x=0, y=0)

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
            self.r3.width = "five"

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
            self.r3.height = "five"

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
            self.r3.x = "five"

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
            self.r3.y = "five"

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
            self.r3.width = 0

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
            self.r3.height = 0

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
            self.r3.x = -45

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
            self.r3.y = -45

        # ensure the exception message is as expected
        self.assertEqual(value_error.exception.__str__(), "y must be >= 0")

    # Test the area method

    def test_area(self):
        """Tests the area method of the Rectangle class."""
        self.assertEqual(self.r1.area(), 20)

        # update the value and try again
        self.r1.width, self.r1.height = 2, 3

        # now check the area again
        self.assertEqual(self.r1.area(), 6)

        # update the r3's value and test with it
        self.r3.width, self.r3.height = 8, 7
        self.assertEqual(self.r3.area(), 56)

    def test_update_method(self):
        """
        Tests the `update()` method.
        """
        self.r1.update(10, 10, 10, 10, 10)
        self.r2.update(id=45, x=4, y=6)

        # test values
        self.assertEqual(self.r1.x, 10)
        self.assertEqual(self.r2.id, 45)
        self.assertEqual(self.r2.x, 4)

    def test_update_method_id_only_positional(self) -> None:
        """
        Tests the `update()` method by setting only the id field using
        positional arguments.
        """
        self.r1.update(35)

        self.assertEqual(self.r1.id, 35)

    def test_update_method_id_only_kwargs(self) -> None:
        """
        Tests the `update()` method by setting only the id field using
        keyword arguments.
        """
        self.r3.update(id=4)

        self.assertEqual(self.r3.id, 4)

    def test_update_method_args_and_kwargs(self) -> None:
        """
        Tests the `update()` method by setting only the id field using
        both positional arguments and keyword arguments. The goal is to test
        which of the two the function uses. The expected is that it used the
        positional argument.
        """
        self.r2.update(20, id=5)

        self.assertEqual(self.r2.id, 20)

    def test_str_method(self) -> None:
        """
        Tests the `__str__()` overloaded method.
        """
        # test the original values first
        expected_result_r1 = "[Rectangle] (1) 0/0 - 10/2"
        expected_result_r2 = "[Rectangle] (2) 0/0 - 2/10"
        expected_result_r3 = "[Rectangle] (12) 0/0 - 10/2"

        self.assertEqual(self.r1.__str__(), expected_result_r1)
        self.assertEqual(self.r2.__str__(), expected_result_r2)
        self.assertEqual(self.r3.__str__(), expected_result_r3)

        # update values and test again
        self.r1.update(id=4, x=2, y=6, width=5)
        expected_result_r1 = "[Rectangle] (4) 2/6 - 5/2"

        # test the current values after update
        self.assertEqual(self.r1.__str__(), expected_result_r1)
