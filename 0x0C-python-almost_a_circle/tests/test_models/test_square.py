#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests the Square class"""

    def setUp(self) -> None:
        self.sq1 = Square(size=5)
        self.sq2 = Square(size=10, x=2, y=3)

    def test_size_value(self) -> None:
        """
        Tests the values assigned to the size attribute of the Square
        class.
        """
        self.assertEqual(self.sq1.size, 5)

        # if the size is correct, then the width and height must be the same
        self.assertEqual(self.sq1.width, self.sq1.size)
        self.assertEqual(self.sq1.width, self.sq1.size)

    def test_set_size(self) -> None:
        """Tests the setting of the size attribute."""
        self.sq1.size = 25

        self.assertEqual(self.sq1.size, 25)

        # if the size is correct, then the width and height must be the same
        self.assertEqual(self.sq1.width, self.sq1.size)
        self.assertEqual(self.sq1.width, self.sq1.size)

    def test_set_size_type_error(self) -> None:
        """
        Tests for TypeError exceptions raised while setting the `size`
        attribute. The exception must be the one raised from the `width`.
        """
        with self.assertRaises(TypeError) as err:
            self.sq1.size = 4.5

        self.assertEqual(err.exception.__str__(), "width must be an integer")

    def test_set_size_value_error(self) -> None:
        """
        Tests for ValueError exceptions raised while setting the `size`
        attribute. The exception must be the one raised from the `width`.
        """
        with self.assertRaises(ValueError) as err:
            self.sq2.size = -3
            self.sq1.size = 0

        self.assertEqual(err.exception.__str__(), "width must be > 0")

    def test_set_size_neg_values_only(self) -> None:
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            self.sq1.size = -5
            self.sq2.size = -19

    def test_set_size_float_values_only(self) -> None:
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.sq1.size = 4.5

    def test_set_size_str_values_only(self) -> None:
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            self.sq1.size = "4"

    def test_to_dictionary(self) -> None:
        """Tests the `to_dictionary()` method."""
        expected_result_sq1 = {"id": self.sq1.id, "x": 0, "y": 0, "size": 5}
        expected_result_sq2 = {"id": self.sq2.id, "x": 2, "y": 3, "size": 10}

        self.assertEqual(self.sq1.to_dictionary(), expected_result_sq1)
        self.assertEqual(self.sq2.to_dictionary(), expected_result_sq2)

    def test_update_invalid_attr(self) -> None:
        """Tests for invalid attribute names passed to the update method."""
        with self.assertRaisesRegex(
            AttributeError, "invalid attribute name: 'p'"
        ):
            self.sq1.update(p=56)

    def test_update_too_many_pos_args(self) -> None:
        """Tests for many positional arguments passed to the update method."""
        with self.assertRaisesRegex(
            ValueError, "excess positional arguments than expected"
        ):
            self.sq2.update(*list(range(10)))

    def test_str_method(self) -> None:
        """
        Tests the `__str__()` overloaded method.
        """
        # test the original values first
        expected_result_sq1 = f"[Square] ({self.sq1.id}) 0/0 - 5"
        expected_result_sq2 = f"[Square] ({self.sq2.id}) 2/3 - 10"

        self.assertEqual(self.sq1.__str__(), expected_result_sq1)
        self.assertEqual(self.sq2.__str__(), expected_result_sq2)

        # update values and test again
        self.sq1.update(id=4, x=2, y=6, size=15)
        expected_result_sq1 = f"[Square] (4) 2/6 - 15"

        # test the current values after update
        self.assertEqual(self.sq1.__str__(), expected_result_sq1)
