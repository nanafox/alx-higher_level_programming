#!/usr/bin/python3

"""
A module with a function that adds an attribute to an object much like
the built-in `setattr()` function
"""


def add_attribute(obj, attribute_name: str, attribute_value) -> None:
    """
    Adds a new attribute to the object if it's possible.

    Args:
        obj: The object to which the attribute will be added.
        attribute_name (str): The name of the new attribute.
        attribute_value: The value of the new attribute.

    Raises:
        TypeError: If the object cannot have new attributes, raises an
        exception with the message "can't add new attribute."

    Tests:
        >>> class TestClass:
        ...     pass

        ==== Create an instance and test expected behaviour ====
        >>> obj1 = TestClass()
        >>> add_attribute(obj1, 'number', 42)
        >>> print(obj1.number)
        42

        ==== Test for errors ====
        >>> obj2 = object()
        >>> add_attribute(obj2, 'number', 42)
        Traceback (most recent call last):
          ...
        TypeError: can't add new attribute
        >>> obj3 = "Hello world"
        >>> add_attribute(obj3, "planet", "earth")
        Traceback (most recent call last):
          ...
        TypeError: can't add new attribute
    """
    if not (
        hasattr(obj, "__dict__")
        or (
            hasattr(type(obj), "__slots__")
            and attribute_name in type(obj).__slots__
        )
    ):
        raise TypeError("can't add new attribute")

    # add or update the attribute with the value
    obj.__dict__[attribute_name] = attribute_value
