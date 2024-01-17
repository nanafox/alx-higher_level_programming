#!/usr/bin/python3

import json
import os
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
        attribute. The exception must be the one raised from the `size`.
        """
        with self.assertRaises(TypeError) as err:
            self.sq1.size = 4.5

        self.assertEqual(err.exception.__str__(), "width must be an integer")

    def test_set_size_value_error(self) -> None:
        """
        Tests for ValueError exceptions raised while setting the `size`
        attribute. The exception must be the one raised from the `size`.
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

    def test_update_one_positional_arg(self) -> None:
        self.sq1.update(1)

        self.assertEqual(self.sq1.id, 1)

    def test_update_two_positional_args(self) -> None:
        self.sq1.update(1, 10)
        self.assertEqual(self.sq1.id, 1)
        self.assertEqual(self.sq1.size, 10)

    def test_update_three_positional_args(self) -> None:
        self.sq1.update(1, 10, 4)
        self.assertEqual(self.sq1.id, 1)
        self.assertEqual(self.sq1.size, 10)
        self.assertEqual(self.sq1.x, 10)

    def test_update_three_positional_args(self) -> None:
        self.sq1.update(1, 4, 10, 3)
        self.assertEqual(self.sq1.id, 1)
        self.assertEqual(self.sq1.size, 4)
        self.assertEqual(self.sq1.x, 10)
        self.assertEqual(self.sq1.y, 3)

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

    def test_str_method_extended(self) -> None:
        self.sq1.update(1, 2, 3)

        expected_result_sq1 = f"[Square] ({self.sq1.id}) 3/0 - 2"
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


class TestSaveToFileOnSquare(unittest.TestCase):
    """Tests the `save_to_file()` class method on Square objects."""

    def setUp(self) -> None:
        try:
            os.remove("Square.json")
        except Exception:
            pass

    def tearDown(self) -> None:
        try:
            os.remove("Square.json")
        except Exception:
            pass

    def test_save_to_file_none_arg(self) -> None:
        """
        Tests the `save_to_file()` class method on a square, argument passed
        is None.
        """
        Square.save_to_file(None)

        try:
            with open("Square.json", "r") as json_file:
                self.assertEqual(json_file.read(), "[]")
        except FileNotFoundError:
            pass

    def test_save_to_file_valid_data(self) -> None:
        """
        Tests the `save_to_file()` class method on a square, argument passed
        is a list of two dictionaries.
        """
        sq1 = Square(size=10, x=7, y=2, id=8)
        sq2 = Square(size=2, x=4, id=2)
        Square.save_to_file([sq1, sq2])

        result = [
            {"id": 8, "x": 7, "size": 10, "y": 2},
            {"id": 2, "x": 4, "size": 2, "y": 0},
        ]

        with open("Square.json", "r") as json_file:
            json_content = json_file.read()
            self.assertEqual(json.dumps(result), json_content)

    def test_save_to_file_attribute_error(self) -> None:
        """
        Tests AttributeError exceptions raise for non-Square objects in list.
        """
        with self.assertRaises(AttributeError):
            Square.save_to_file([4, "54"])


class TestFromJsonStringOnSquare(unittest.TestCase):
    """Tests the `from_json_string() static method on Square objects."""

    def setUp(self) -> None:
        self.sq1 = Square(size=5, id=1)
        self.sq2 = Square(size=10, x=2, y=3, id=2)

    def test_from_json_to_string_none_arg(self) -> None:
        """Tests for empty lists when None is passed as argument."""
        self.assertEqual(Square.from_json_string(None), [])

    def test_from_json_to_string_non_json_string(self) -> None:
        """Tests encoding errors for non-JSON strings."""
        with self.assertRaises(json.decoder.JSONDecodeError):
            Square.from_json_string("Hello")

    def test_from_json_string_integer_arg(self) -> None:
        """Tests for TypeError raised when an integer is passed as argument."""
        with self.assertRaisesRegex(TypeError, "must be a string"):
            Square.from_json_string(87)

    def test_from_json_string_list_arg(self) -> None:
        """Tests for TypeError raised when a list is passed as argument."""
        with self.assertRaisesRegex(TypeError, "must be a string"):
            Square.from_json_string(["Hello"])

    def test_from_json_string_empty_list(self) -> None:
        """Tests for when an empty list is passed as argument."""
        self.assertEqual(Square.from_json_string("[]"), [])

    def test_from_json_string_size_only_set(self) -> None:
        """
        Tests for when a valid JSON string is passed with only the size set.
        """
        dictionary = self.sq1.to_dictionary()
        json_str = Square.to_json_string([dictionary])

        expected_result = [{"id": 1, "x": 0, "size": 5, "y": 0}]
        self.assertEqual(Square.from_json_string(json_str), expected_result)

    def test_from_json_string_size_xy_set(self) -> None:
        """
        Tests for when a valid JSON string is passed with the size,
        x, and y values set.
        """
        dictionary = self.sq2.to_dictionary()
        json_str = Square.to_json_string([dictionary])

        expected_result = [{"id": 2, "x": 2, "size": 10, "y": 3}]
        self.assertEqual(Square.from_json_string(json_str), expected_result)

    def test_from_json_string_none_arg(self) -> None:
        """Tests for None type args passed to `from_json_string()` method."""
        self.assertEqual(Square.from_json_string(None), [])

    def test_from_json_string_empty_list(self) -> None:
        """Tests for empty lists passed to `from_json_string()` method."""
        self.assertEqual(Square.from_json_string(None), [])


class TestSquareInstantiationErrors(unittest.TestCase):
    """
    Tests multiple errors that occur during Square object instantiation.
    """

    def test_invalid_init_size_str_value(self) -> None:
        """
        Tests string values passed as `size` during object instantiation.
        """
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Square(size="1")

    def test_negative_init_size_value(self) -> None:
        """
        Tests negative values passed as `size` during object instantiation.
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(size=-3)

    def test_init_zero_width_value(self) -> None:
        """
        Tests zero values given as `size` during during object instantiation.
        """
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(size=0)

    def test_invalid_init_x_value(self) -> None:
        """
        Tests string values passed as `x` during object instantiation.
        """
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Square(size=3, x="1")

    def test_invalid_init_y_value(self) -> None:
        """
        Tests string values passed as `y` during object instantiation.
        """
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Square(size=3, x=1, y="2")

    def test_negative_init_x_value(self) -> None:
        """
        Tests negative values passed as `x` during object instantiation.
        """
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(size=3, x=-4)

    def test_negative_init_y_value(self) -> None:
        """
        Tests negative values passed as `y` during object instantiation.
        """
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(size=3, x=3, y=-4)
