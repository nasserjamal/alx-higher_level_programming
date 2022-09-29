#!/usr/bin/python3
"""Test module for the base module"""


import unittest
from models.base import Base


class test_Base(unittest.TestCase):
    """Test class for the test class"""

    def test_Base_Init(self):
        """Testing Base class initialization"""
        new_base = Base()
        self.assertEqual(new_base.id, 1)
        new_base2 = Base(10)
        self.assertEqual(new_base2.id, 10)
        new_base3 = Base()
        self.assertEqual(new_base3.id, 2)
