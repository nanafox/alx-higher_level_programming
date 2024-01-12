#!/usr/bin/python3
"""A module that defines a Square and inherits from the Rectangle class."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Models a Square object."""

    def __init__(self, size, x=0, y=0, id=None) -> None:
        super().__init__(size, size, x, y, id)
        self.size = self.width

    def __str__(self) -> str:
        """
        Returns information about the Rectangle instance.

        Returns:
            str: Information about the Rectangle instance.
        """
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.size}"
        )
