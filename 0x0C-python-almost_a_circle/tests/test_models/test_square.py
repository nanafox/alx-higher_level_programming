#!/usr/bin/python3

import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Tests the Square class"""

    sq1 = Square(size=5)
    sq2 = Square(size=10, x=2, y=3)

    def tearDown(self) -> None:
        self.sq1.update(size=5)
        self.sq2.update(size=10, x=2, y=3)

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

    def test_to_dictionary(self) -> None:
        """Tests the `to_dictionary()` method."""
        expected_result_sq1 = {"id": self.sq1.id, "x": 0, "y": 0, "size": 5}
        expected_result_sq2 = {"id": self.sq2.id, "x": 2, "y": 3, "size": 10}

        self.assertEqual(self.sq1.to_dictionary(), expected_result_sq1)
        self.assertEqual(self.sq2.to_dictionary(), expected_result_sq2)
