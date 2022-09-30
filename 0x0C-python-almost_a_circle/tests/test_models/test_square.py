#!/usr/bin/python3
"""Test module for the square module"""


import unittest

from models.rectangle import Rectangle
from models.square import Square


class test_Square(unittest.TestCase):
    """Test class: Testing the Square class"""
    def setUp(self) -> None:
        self.my_square = Square(3, 1, 2, 5)

    def test_init(self):
        """Testing square initialization"""
        self.assertEqual(self.my_square.width, 3)
        self.assertEqual(self.my_square.height, 3)
        self.assertEqual(self.my_square.x, 1)
        self.assertEqual(self.my_square.y, 2)
        self.assertEqual(self.my_square.id, 5)

    def test_inheritance(self):
        """Testing if it inherits from the rectangle class"""
        self.assertIsInstance(self.my_square, Rectangle)

    def test_str(self):
        """Testing the __str__ literals"""
        self.assertEqual(str(self.my_square), "[Square] ({}) \
{}/{} - {}".format(5, 1, 2, 3))

    def test_size_attr(self):
        """Testing the size attribute: Getter and setter"""
        self.assertEqual(self.my_square.size, 3)
        self.my_square.size = 8
        self.assertEqual(self.my_square.size, 8)
        self.assertEqual(self.my_square.width, 8)
        self.assertEqual(self.my_square.height, 8)

        with self.assertRaises(TypeError) as msg:
            self.my_square.size = [1, 2]
            self.assertTrue('width must be an integer' in str(msg.exception))

        with self.assertRaises(ValueError) as msg:
            self.my_square.size = -1
            self.assertTrue('width must be > 0' in str(msg.exception))

    def test_update(self):
        """Testing the update method"""
        self.my_square.update(12)
        self.assertEqual(str(self.my_square), "[Square] ({}) \
{}/{} - {}".format(12, 1, 2, 3))

        self.my_square.update(19, 2, 4, 5, width=1)
        self.assertEqual(str(self.my_square), "[Square] ({}) \
{}/{} - {}".format(19, 4, 5, 2))

        self.my_square.update(x=1, size=2, y=3)
        self.assertEqual(str(self.my_square), "[Square] ({}) \
{}/{} - {}".format(19, 1, 3, 2))

    def test_to_dictionary(self):
        """Testing the to_dictionary method"""
        self.assertEqual(self.my_square.to_dictionary(), {'id': 5, 'size': 3, 'x': 1, 'y': 2})
