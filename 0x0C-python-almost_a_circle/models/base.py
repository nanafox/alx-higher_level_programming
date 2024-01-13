#!/usr/bin/python3
"""Defines the base class class for future classes."""

import json


class Base:
    """Base object for future classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base object.

        Args:
            id (int, optional): The ID of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries: "list[dict]") -> str:
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list[dict]): The list of dictionaries.

        Returns:
            str: The JSON string representation of objects in the
            `list_dictionaries` else "[]" if empty.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        if type(list_dictionaries) is not list:
            raise TypeError("list_dictionaries must be a list of dictionaries")

        for obj in list_dictionaries:
            if type(obj) is not dict:
                raise TypeError(
                    "list_dictionaries must be a list of dictionaries"
                )

        return json.dumps(list_dictionaries)
