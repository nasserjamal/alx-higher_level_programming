#!/usr/bin/python3
"""Test module for the base module"""


import unittest
from models.base import Base
from models.rectangle import Rectangle
from unittest.mock import patch, mock_open


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
        r1 = Rectangle(10, 7, 2, 8, 3)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(json_dictionary, '[{"id": 3, "width": 10, "height": 7, "x": 2, "y": 8}]')

    def test_save_to_file(self):
        """Testing saving to file"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        open_mock = mock_open()
        with patch("models.Base", open_mock, create=True):
            Rectangle.save_to_file([r1, r2])

        open_mock.assert_called_with("Rectangle.json", "w")
        open_mock.return_value.write.assert_called_once_with('\
[{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]')
