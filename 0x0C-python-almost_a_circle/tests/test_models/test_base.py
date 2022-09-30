#!/usr/bin/python3
"""Test module for the base module"""


import unittest
from models.base import Base
from models.rectangle import Rectangle


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

    def test_to_json_string(self):
        """Test the to_json_string method"""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 3, "width": 10, "height": 7, "x": 2, "y": 8}]')
