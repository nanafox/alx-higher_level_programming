#!/usr/bin/python3


import unittest

Rectangle = __import__("2-rectangle").Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self) -> None:
        self.rectangle_1 = Rectangle(2, 4)
        self.rectangle_2 = Rectangle(8, 16)
        self.rectangle_3 = Rectangle(0, 6)
        self.rectangle_4 = Rectangle(6, 0)

    def tearDown(self) -> None:
        pass

    def test_width_set_success(self) -> None:
        """Tests the successful setting and updates of the rectangle's width"""
        self.assertEqual(self.rectangle_1.width, 2)
        self.assertEqual(self.rectangle_2.width, 8)
        self.assertEqual(self.rectangle_3.width, 0)

        # update the width
        self.rectangle_1.width = 8
        self.rectangle_2.width = 4

        # check the current width
        self.assertEqual(self.rectangle_1.width, 8)
        self.assertEqual(self.rectangle_2.width, 4)

    def test_width_set_failure(self) -> None:
        """Tests the failure of setting and updates of the rectangle's width"""
        with self.assertRaises(TypeError):
            Rectangle("1")  # try with string
            Rectangle([9, 3])  # try with a list
            Rectangle(4.3, 8.3)  # try with floats

        with self.assertRaises(ValueError):
            Rectangle(-34)
            Rectangle(-92)

    def test_height_set_success(self) -> None:
        """
        Tests the success of setting and updates of the rectangle's
        height
        """
        self.assertEqual(self.rectangle_1.height, 4)
        self.assertEqual(self.rectangle_2.height, 16)
        self.assertEqual(self.rectangle_4.height, 0)

        # update the width
        self.rectangle_1.height = 8
        self.rectangle_2.height = 2

        # check the current width
        self.assertEqual(self.rectangle_1.height, 8)
        self.assertEqual(self.rectangle_2.height, 2)

    def test_height_set_failure(self) -> None:
        """
        Tests the failure of setting and updates of the rectangle's
        height
        """
        with self.assertRaises(TypeError):
            Rectangle(1, "5")  # try with string
            Rectangle(5, [9, 3])  # try with a list
            Rectangle(4.3, 8.3)  # try with floats

        with self.assertRaises(ValueError):
            Rectangle(3, -6)
            Rectangle(8, -16)

    def test_area(self) -> None:
        """Tests the area() instance method"""
        self.assertEqual(self.rectangle_1.area(), 8)
        self.assertEqual(self.rectangle_2.area(), 128)
        self.assertEqual(self.rectangle_3.area(), 0)

    def test_perimeter(self) -> None:
        """Tests the perimeter() instance method"""
        self.assertEqual(self.rectangle_1.perimeter(), 12)
        self.assertEqual(self.rectangle_3.perimeter(), 0)
