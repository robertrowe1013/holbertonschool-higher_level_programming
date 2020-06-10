#!/usr/bin/python
"""rectangel tests"""
import unittest
from models.rectangle import Rectangle


class TestRectangleMethods(unittest.TestCase):
    """rectangle tests"""

    def test_rectangle(self):
        """retangle test sucesses"""
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        r4 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r4.id, 12)

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
