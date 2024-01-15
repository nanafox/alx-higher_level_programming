#!/usr/bin/python3

import json
import sys
import unittest
from io import StringIO
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


class TestToJsonStringOnSquare(unittest.TestCase):
    """Tests the `to_json_string` static method on the Square class."""

    def setUp(self) -> None:
        self.sq1 = Square(size=5)
        self.sq2 = Square(size=10, x=2, y=3)

    def test_to_json_square_for_one(self) -> None:
        """
        Tests the `to_json_string` method on the Square class for
        one object.
        """
        dictionary = self.sq1.to_dictionary()

        self.assertEqual(
            Square.to_json_string([dictionary]), json.dumps([dictionary])
        )

    def test_to_json_square_for_multiple(self) -> None:
        """
        Tests the `to_json_string` method on the Square class for multiple
        objects.
        """
        dictionary_1 = self.sq1.to_dictionary()
        dictionary_2 = self.sq2.to_dictionary()

        self.assertEqual(
            Square.to_json_string([dictionary_1, dictionary_2]),
            json.dumps([dictionary_1, dictionary_2]),
        )

    def test_to_json_string_not_list(self) -> None:
        """
        Tests for TypeError exception raised when the argument passed is not
        a list.
        """
        with self.assertRaises(TypeError):
            Square.to_json_string("not list")

    def test_to_json_string_not_list_of_dicts(self) -> None:
        """
        Tests for TypeError exception raised when the argument passed is not
        a list of dictionaries.
        """
        with self.assertRaises(TypeError):
            Square.to_json_string(
                list_dictionaries=[34, 9, self.sq1.to_dictionary()]
            )

    def test_to_json_string_return_type(self) -> None:
        self.assertTrue(
            type(Square.to_json_string([self.sq1.to_dictionary()])) is str
        )


class TestDisplayOnSquare(unittest.TestCase):
    def setUp(self) -> None:
        self.sq1 = Square(size=5)
        self.sq2 = Square(size=10, x=2, y=3)

    def test_display_square_with_size_one(self) -> None:
        """
        Tests the `display()` for a square of size one (1), and no
        `x`or `y` values.
        """
        self.sq1.size = 1
        captured = StringIO()
        sys.stdout = captured
        self.sq1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured.getvalue(), "#\n")

    def test_display_for_size_five(self) -> None:
        """
        Tests the `display()` for a square of size five(5)
        no `x`or `y` values.
        """
        expected_result = "#####\n#####\n#####\n#####\n#####\n"
        captured = StringIO()
        sys.stdout = captured
        self.sq1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured.getvalue(), expected_result)

    def test_display_with_x(self) -> None:
        """
        Tests the `display()` for a square of size five(5) and `x` value 3
        and no `y` value.
        """
        self.sq1.x = 3
        expected_result = "   #####\n   #####\n   #####\n   #####\n   #####\n"
        captured = StringIO()
        sys.stdout = captured
        self.sq1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured.getvalue(), expected_result)

    def test_display_with_y(self) -> None:
        """
        Tests the `display()` for a square of size five(5) and `y` value 3
        and not `x` value.
        """
        self.sq1.y = 3
        expected_result = "\n\n\n#####\n#####\n#####\n#####\n#####\n"
        captured = StringIO()
        sys.stdout = captured
        self.sq1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured.getvalue(), expected_result)

    def test_display_with_size_x_and_y(self) -> None:
        """
        Tests the display method with `size`, `x` and `y` values set.
        """
        self.sq1.update(x=3, y=3)
        expected_result = (
            "\n\n\n   #####\n   #####\n   #####\n   #####\n   #####\n"
        )
        captured = StringIO()
        sys.stdout = captured
        self.sq1.display()
        sys.stdout = sys.__stdout__

        self.assertEqual(captured.getvalue(), expected_result)
