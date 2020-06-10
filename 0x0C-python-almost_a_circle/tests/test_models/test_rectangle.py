#!/usr/bin/python
"""rectangel tests"""
import unittest
from models.rectangle import Rectangle

class TestRectangleMethods(unittest.TestCase):
    """rectangle tests"""
    def test_rectangle(self):
        """retangle tests"""
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
