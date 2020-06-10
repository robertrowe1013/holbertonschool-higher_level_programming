#!/usr/bin/python
"""rectangel tests"""
import unittest
from models.square import Square


class TestSquareMethods(unittest.TestCase):
    """square tests"""

    def test_square(self):
        """square test sucesses"""
        s1 = Square(10, 0, 0, 12)
        self.assertEqual(s1.id, 12)
        s2 = Square(size=1, id=12)
        self.assertEqual(s2.id, 12)

    def test_square_te(self):
        """square type errors"""
        with self.assertRaises(TypeError):
            Square("2")
        with self.assertRaises(TypeError):
            Square(2.5)
        with self.assertRaises(TypeError):
            Square(None)
        with self.assertRaises(TypeError):
            Square(1, "1", 1, 1)
        with self.assertRaises(TypeError):
            Square(1, 1, "1", 1)
        with self.assertRaises(TypeError):
            Square(1, 1, 1, 1, 1, 1)
        with self.assertRaises(TypeError):
            Square(depth=1)
        with self.assertRaises(TypeError):
            Square()
        with self.assertRaises(TypeError):
            Square(height=1)

    def test_square_ve(self):
        """square value errors"""
        with self.assertRaises(ValueError):
            Square(-1)
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(1, -1)
        with self.assertRaises(ValueError):
            Square(1, 1, -1)
        with self.assertRaises(TypeError):
            Square(1.1)
        with self.assertRaises(TypeError):
            Square(1, 1.1)
        with self.assertRaises(TypeError):
            Square(1, 1, 1.1)

    def test_rectangle_mods(self):
        """mod checks"""
        s3 = Square(2)
        self.assertEqual(s3.area(), 4)
