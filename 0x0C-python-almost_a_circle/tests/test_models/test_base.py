#!/usr/bin/python3
"""Tests the Base class in the models package."""

from models.base import Base
import unittest


class TestBaseClass(unittest.TestCase, Base):
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
