#!/usr/bin/python3
"""Defines the base class for future classes."""

import csv
import os
import json
import turtle


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
            with open(f"{cls.__name__}.json", "w") as json_file:
                json_file.write("[]")

            return

        if cls.__name__ not in ["Rectangle", "Square"]:
            raise TypeError("invalid object type")

        try:
            with open(f"{cls.__name__}.json", "w") as json_file:
                list_dictionaries = [obj.to_dictionary() for obj in list_objs]
                json_file.write(cls.to_json_string(list_dictionaries))
        except FileNotFoundError:
            pass

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

    @classmethod
    def save_to_file_csv(cls, list_objs: list) -> None:
        """
        Writes the CSV string representation of a list of objects to a file.

        Args:
            list_objs (list): The list of objects that inherits from `Base`.

        Raises:
            TypeError: If any of the objects in `list_objs` is not an instance
            of the `Base` class.
        """
        with open(f"{cls.__name__}.csv", "w") as csv_file:
            if list_objs is None or len(list_objs) == 0:
                csv_file.write("[]")
                return

            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            elif not issubclass(cls, Base):
                raise TypeError("incompatible object type")

            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Returns a list of instances from a CSV file.

        Returns:
            list: A list of instances from a CSV file.
        """
        instances = []
        try:
            file_name = f"{cls.__name__}.csv"
            if os.path.exists(file_name):
                with open(file_name, "r", newline="") as csv_file:
                    rows = []
                    if cls.__name__ == "Rectangle":
                        fieldnames = ["id", "width", "height", "x", "y"]
                    elif cls.__name__ == "Square":
                        fieldnames = ["id", "size", "x", "y"]
                    elif not issubclass(cls, Base):
                        raise TypeError("Incompatible object type")

                    reader = csv.DictReader(csv_file)
                    for row in reader:
                        for data in row:
                            row[data] = int(row[data])
                        rows.append(row)

                    instances = [cls.create(**obj) for obj in rows]
        except FileNotFoundError:
            return []

        return instances

    @classmethod
    def draw(cls, list_rectangles, list_squares) -> None:
        """Draw rectangles and squares side by side using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        screen = turtle.Screen()
        screen.bgcolor("#180302")
        screen.title("Shapes | theLazyProgrammer^_^")

        drawer = turtle.Turtle()
        drawer.pensize(5)
        drawer.shape("circle")
        drawer.speed(5)

        cls._draw_shapes(drawer, list_rectangles, "#f4f45d", side_by_side=True)
        cls._draw_shapes(drawer, list_squares, "#0670d4", side_by_side=True)

        turtle.exitonclick()

    @staticmethod
    def _draw_shapes(turtle_drawer, shapes, color, side_by_side=False) -> None:
        """Draw a list of shapes using the turtle module.

        Args:
            turtle_drawer (turtle.Turtle): The turtle used for drawing.
            shapes (list): A list of shapes (Rectangle or Square objects) to
            draw.
            color (str): The color to use for drawing.
            side_by_side (bool): Whether to draw shapes side by side.
        """
        turtle_drawer.color(color)

        for shape in shapes:
            turtle_drawer.showturtle()
            turtle_drawer.up()

            if side_by_side:
                if shape.__class__.__name__ == "Square":
                    turtle_drawer.goto(shape.x + shape.size, shape.y)
                elif shape.__class__.__name__ == "Rectangle":
                    turtle_drawer.goto(shape.x + shape.width, shape.y)
            else:
                turtle_drawer.goto(shape.x, shape.y)

            turtle_drawer.down()
            if shape.__class__.__name__ == "Square":
                for _ in range(4):
                    turtle_drawer.forward(shape.size)
                    turtle_drawer.left(90)
            elif shape.__class__.__name__ == "Rectangle":
                for _ in range(2):
                    turtle_drawer.forward(shape.width)
                    turtle_drawer.left(90)
                    turtle_drawer.forward(shape.height)
                    turtle_drawer.left(90)

            turtle_drawer.hideturtle()
