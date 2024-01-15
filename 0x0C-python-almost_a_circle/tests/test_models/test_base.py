#!/usr/bin/python3
"""Tests the Base class in the models package."""

import json
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBaseClass(unittest.TestCase):
    """Tests the Base class."""

    b1 = Base()
    b2 = Base()
    b3 = Base(45)
    b4 = Base(12)
    b5 = Base()
    b6 = Base(98)

    def test_automatic_id(self):
        """Tests the ID when it is not provided (Generated automatically)."""
        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b5.id, 3)

    def test_manual_id(self):
        """Tests when the ID is provided by the user."""
        self.assertEqual(self.b3.id, 45)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b6.id, 98)

    def test_automatic_and_manual(self):
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
