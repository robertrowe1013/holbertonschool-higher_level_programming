#!/usr/bin/python3
"""unittest tests"""


import unittest
max_int = __import__('6-max_integer').max_integer

class Test6(unittest.TestCase):
    """test task 6"""

    def test_max(self):
        self.assertEqual(max_int([1, 2]), 2)
        self.assertEqual(max_int([2, 1]), 2)
        self.assertEqual(max_int([1, 2, 0]), 2)
        self.assertEqual(max_int([-1, 2]), 2)
        self.assertEqual(max_int([-1, -2]), -1)
        self.assertEqual(max_int([2]), 2)
