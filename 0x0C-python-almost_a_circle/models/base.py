#!/usr/bin/python3
"""Defines the base class for future classes."""

import os
import json


class Base:
    """Base object for future classes."""

    __nb_objects = 0

    def __init__(self, id=None) -> None:
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

        Raises:
            TypeError: If the argument received `list_dictionaries` is not a
            list or does not contain a list of dictionaries.

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

    @classmethod
    def save_to_file(cls, list_objs: list) -> None:
        """
        Writes the JSON string representation of a list of objects to a file.

        `list_objs` is a list of instances who inherits from the `Base` class.
        This function uses the concept of polymorphism so it allows for a list
        of mixed objects that inherits from `Base`.

        Args:
            list_objs (list): The list of objects that inherits from `Base`.

        Raises:
            TypeError: If any of the objects in `list_objs` is not an instance
            of the `Base` class.
        """
        if list_objs is None or len(list_objs) == 0:
            with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
                file.write("[]")

            return

        dict_of_objs = {}

        for obj in list_objs:
            if not isinstance(obj, Base):
                raise TypeError(
                    "list_objs must be a list of objects who inherit from Base"
                )

            class_name = obj.__class__.__name__
            if class_name not in dict_of_objs:
                dict_of_objs[class_name] = []

            dict_of_objs[class_name].append(obj.to_dictionary())

        for class_name, list_dictionaries in dict_of_objs.items():
            json_dictionary = cls.to_json_string(list_dictionaries)
            with open(f"{class_name}.json", "w", encoding="utf-8") as file:
                json.dump(json.loads(json_dictionary), file)

    @staticmethod
    def from_json_string(json_string: str) -> list:
        """
        Returns the JSON representation of a JSON-formatted string.

        Args:
            json_string (str): The JSON-formatted string representation.

        Returns:
            list: A list of JSON representation of `json_string`.
        """
        if json_string is None:
            return []

        if type(json_string) is not str:
            raise TypeError("json_string must be a string")

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary: dict):
        """
        Returns a Rectangle instance with all attributes already set.

        Returns:
            Rectangle: An instance with all of its attributes already
            set using `dictionary`.
        """
        dummy = None

        if cls.__name__ == "Rectangle":
            dummy = cls(4, 8)  # create a Rectangle object
        elif cls.__name__ == "Square":
            dummy = cls(8)  # create a Square object

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls) -> list:
        """
        Returns a list of instances from a JSON file.

        Returns:
            list: A list of instances from a JSON file.
        """
        instances = []
        try:
            if os.path.exists(f"{cls.__name__}.json"):
                with open(
                    f"{cls.__name__}.json", "r", encoding="utf-8"
                ) as json_file:
                    content = json_file.read()

                list_dictionaries = cls.from_json_string(content)
                for dictionary in list_dictionaries:
                    instances.append(cls.create(**dictionary))
        except FileNotFoundError:
            return []

        return instances
