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
        Returns information about the Square instance.

        Returns:
            str: Information about the Square instance.
        """
        return (
            f"[{self.__class__.__name__}] ({self.id}) "
            f"{self.x}/{self.y} - {self.size}"
        )

    @property
    def size(self) -> int:
        """
        Returns the size of the Square instance.

        Returns:
            int: The size of the Square instance.
        """
        return self.width

    @size.setter
    def size(self, value: int) -> None:
        """
        Sets and updates the `size` attribute of the Square instance.

        Args:
            value (int): The value to use as the new size.
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs) -> None:
        """
        Updates attributes with the values in the provided `args` or `kwargs`.
        """
        if args is not None and len(args) > len(self.__dict__.keys()):
            raise ValueError("excess positional arguments than expected")

        if args is not None and len(args) > 0:
            obj_dict_keys = list(self.to_dictionary().keys())
            obj_dict_keys.sort()

            for i, value in enumerate(args):
                setattr(self, obj_dict_keys[i], value)
            return

        # use the keyword arguments instead since the *args was unavailable
        for attr, value in kwargs.items():
            if not hasattr(self, attr):
                raise AttributeError(f"invalid attribute name: '{attr}'")

            setattr(self, attr, value)

    def to_dictionary(self) -> dict:
        """
        Returns the dictionary representation of a Square instance.

        Returns:
            dict: The dictionary representation of a Square instance.
        """
        return {
            "id": self.id,
            "x": self.x,
            "size": self.width,
            "y": self.y,
        }
