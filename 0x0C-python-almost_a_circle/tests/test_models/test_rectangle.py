#!/usr/bin/python
"""rectangel tests"""
import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """rectangle tests"""

    def test_rectangle(self):
        """retangle test sucesses"""
        r1 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 12)
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)

    def test_rectangle_te(self):
        """rectangle type errors"""
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        with self.assertRaises(TypeError):
            Rectangle("10", 2)
        with self.assertRaises(TypeError):
            Rectangle(10, None)
        with self.assertRaises(TypeError):
            Rectangle(1.4, 2)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, "1", 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, "1", 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            Rectangle(depth=1)
        with self.assertRaises(TypeError):
            Rectangle()
        with self.assertRaises(TypeError):
            Rectangle(1)

    def test_rectangle_ve(self):
        """rectangle value errors"""
        with self.assertRaises(ValueError):
            Rectangle(-1, 1)
        with self.assertRaises(ValueError):
            Rectangle(1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, -1)
        with self.assertRaises(ValueError):
            Rectangle(1, 1, 1, -1)
        with self.assertRaises(TypeError):
            Rectangle(1.1, 1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1.1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1.1)
        with self.assertRaises(TypeError):
            Rectangle(1, 1, 1, 1.1)

    def test_rectangle_mods(self):
        """mod checks"""
        r3 = Rectangle(2, 3)
        self.assertEqual(r3.area(), 6)
