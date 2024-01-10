#!/usr/bin/python3

"""A module that models a Student object."""


class Student:
    """Models a Student object."""

    def __init__(self, first_name: str, last_name: str, age: int) -> None:
        """
        Initializes / creates a new Student object.

        Args:
            first_name (str): The student's first name.
            last_name (str): The student's last name.
            age (int): The student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attr=None) -> dict:
        """
        Returns the dictionary representation of the `Student` object.

        Args:
            attr: A list of attribute names to retrieve.

        Returns:
            dict: The dictionary representation of the `Student` object.
        """
        if attr is not None and isinstance(attr, list):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attr
            }

        # no specific attributes were given, return everything
        return self.__dict__

    def reload_from_json(self, json: dict) -> None:
        """
        Replaces all attributes of a `Student` instance with contents in a
        JSON file.

        Args:
            json (dict): The JSON file containing the `__dict__`-like
            structure of a Student object.
        """
        for key, value in json.items():
            self.__dict__[key] = value
