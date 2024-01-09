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

    def to_json(self) -> dict:
        """Returns the dictionary representation of the Student object."""
        return self.__dict__
