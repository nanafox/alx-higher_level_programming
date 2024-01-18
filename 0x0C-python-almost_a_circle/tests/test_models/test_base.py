#!/usr/bin/python3
"""Tests the Base class in the models package."""

import json
import inspect
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestDocumentation(unittest.TestCase):
    """Tests the documentation for modules, classes and methods."""

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up class method for the doc tests.
        """
        cls.setup = inspect.getmembers(Base, inspect.isfunction)

    def test_module_docstring_exists(self):
        """
        Tests if module docstring documentation exists.
        """
        self.assertIsNotNone(Base.__doc__)

    def test_classes_docstring_exists(self):
        """
        Tests if class docstring documentation exists.
        """
        self.assertIsNotNone(Base.__doc__.__class__)

    def test_methods_docstring_exists(self):
        """
        Tests if methods docstring documentation exists
        """
        for _, method in self.setup:
            self.assertIsNotNone(method.__doc__)


class TestBaseClass(unittest.TestCase):
    """Tests the Base class."""

    b1 = Base()
    b2 = Base()
    b3 = Base(45)
    b4 = Base(12)
    b5 = Base()
    b6 = Base(98)

    def test_automatic_id(self) -> None:
        """Tests the ID when it is not provided (Generated automatically)."""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b5.id, 3)

    def test_manual_id(self) -> None:
        """Tests when the ID is provided by the user."""
        self.assertEqual(self.b3.id, 45)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b6.id, 98)

    def test_automatic_and_manual(self) -> None:
        """Tests cases when the ID is provided and when it is not."""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 45)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 3)
        self.assertEqual(self.b6.id, 98)

    def test_valid_to_json_string(self) -> None:
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        expected_result = json.dumps([dictionary])

        self.assertEqual(json_dictionary, expected_result)

    def test_multi_valid_to_json_string(self) -> None:
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(3, 6, 4, 1)
        dictionary_1 = r1.to_dictionary()
        dictionary_2 = r2.to_dictionary()

        json_dictionary = Base.to_json_string([dictionary_1, dictionary_2])
        expected_result = json.dumps([dictionary_1, dictionary_2])

        self.assertEqual(json_dictionary, expected_result)

    def test_empty_list_to_json_string(self) -> None:
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_none_arg_to_json_string(self) -> None:
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_not_list_arg_to_json_string(self) -> None:
        """
        Tests the `to_json_string` static method using invalid arguments of
        pass a list.
        """
        with self.assertRaises(TypeError) as err:
            Base.to_json_string("not list")
            (Base.to_json_string(89))
            Base.to_json_string({"name": "Bob"})

        self.assertEqual(
            err.exception.__str__(),
            "list_dictionaries must be a list of dictionaries",
        )

    def test_not_list_of_dict_arg_to_json_string(self) -> None:
        with self.assertRaises(TypeError) as err:
            Base.to_json_string([4, "8", (1, 2, 3)])
            (Base.to_json_string([[1, 2, 3], {4, 5, 6}]))
            Base.to_json_string([{"name": "Bob"}, "something else"])

        self.assertEqual(
            err.exception.__str__(),
            "list_dictionaries must be a list of dictionaries",
        )

    def test_no_args_to_json_string(self) -> None:
        with self.assertRaises(TypeError) as err:
            Base.to_json_string()

        self.assertEqual(
            err.exception.__str__(),
            "to_json_string() missing 1 required positional argument: "
            "'list_dictionaries'",
        )


class TestFromJsonStringBase(unittest.TestCase):
    """Tests the `from_json_string() static method on Base."""

    def test_from_json_to_string_none_arg(self) -> None:
        """Tests for empty lists when None is passed as argument."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty_list(self) -> None:
        """Tests for when an empty list is passed as argument."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_to_string_non_json_string(self) -> None:
        """Tests encoding errors for non-JSON strings."""
        with self.assertRaises(json.decoder.JSONDecodeError):
            Base.from_json_string("Hello")

    def test_from_json_string_integer_arg(self) -> None:
        """Tests for TypeError raised when an integer is passed as argument."""
        with self.assertRaisesRegex(TypeError, "must be a string"):
            Base.from_json_string(87)

    def test_from_json_string_list_arg(self) -> None:
        """Tests for TypeError raised when a list is passed as argument."""
        with self.assertRaisesRegex(TypeError, "must be a string"):
            Base.from_json_string(["Hello"])

    def test_from_json_string_valid_data(self) -> None:
        """Tests for valid data passed to `from_json_string_method`."""
        self.assertEqual(Base.from_json_string('[{"id": 5}]'), [{"id": 5}])
