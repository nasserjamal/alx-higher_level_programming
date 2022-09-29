#!/usr/bin/python3
"""Test module for recatngle module"""


from io import StringIO
from turtle import width
import unittest
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class test_Rectangle(unittest.TestCase):
    """Test class to test the Recatngle class"""

    def setUp(self):
        self.my_rect = Rectangle(3, 2, 1, 1, 10)

    def test_initialization(self):
        """Testing Rectangle class initialization"""
        rect1 = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(rect1.width, 1)
        self.assertEqual(rect1.height, 2)
        self.assertEqual(rect1.x, 3)
        self.assertEqual(rect1.y, 4)
        self.assertEqual(rect1.id, 5, "Id is not properly declared")

    def test_inheritance(Self):
        """Test if it inherits from base class"""
        Self.assertIsInstance(Rectangle(1, 2), Base)

    def test_2Args(self):
        """Testing Rectangle with two arguments"""
        my_rect = Rectangle(1, 2)
        self.assertEqual(my_rect.width, 1)
        self.assertEqual(my_rect.height, 2)
        self.assertEqual(my_rect.x, 0)
        self.assertEqual(my_rect.y, 0)
        self.assertEqual(my_rect.id, 1, "Id is not properly declared")

    def test_invalid_width(self):
        """Testing with invalid width"""
        with self.assertRaises(TypeError) as msg:
            Rectangle("1", 2)
        self.assertTrue('width must be an integer' in str(msg.exception))

        with self.assertRaises(ValueError) as msg:
            Rectangle(0, 2)
        self.assertTrue('width must be > 0' in str(msg.exception))

        with self.assertRaises(ValueError) as msg:
            Rectangle(-5, 2)
        self.assertTrue('width must be > 0' in str(msg.exception))

    def test_invalid_height(self):
        """Testing with invalid height"""
        with self.assertRaises(TypeError) as msg:
            Rectangle(1, "2")
        self.assertTrue('height must be an integer' in str(msg.exception))

        with self.assertRaises(ValueError) as msg:
            Rectangle(1, 0)
        self.assertTrue('height must be > 0' in str(msg.exception))

        with self.assertRaises(ValueError) as msg:
            Rectangle(1, -2)
        self.assertTrue('height must be > 0' in str(msg.exception))

    def test_invalid_x(self):
        """Testing with invalid x"""
        with self.assertRaises(TypeError) as msg:
            Rectangle(1, 2, [1, 2])
        self.assertTrue('x must be an integer' in str(msg.exception))

        with self.assertRaises(ValueError) as msg:
            Rectangle(1, 2, -1)
        self.assertTrue('x must be >= 0' in str(msg.exception))

    def test_invalid_x(self):
        """Testing with invalid y"""
        with self.assertRaises(TypeError) as msg:
            Rectangle(1, 2, 0, [1, 2])
        self.assertTrue('y must be an integer' in str(msg.exception))

        with self.assertRaises(ValueError) as msg:
            Rectangle(1, 2, 0, -1)
        self.assertTrue('y must be >= 0' in str(msg.exception))

    def test_area(self):
        """Testing the area method"""
        self.assertEqual(self.my_rect.area(), 6)

    def test_display(self):
        """Testing output of the method display"""
        with patch('sys.stdout', new=StringIO()) as output:
            self.my_rect.display()
            self.assertEqual(output.getvalue(), "\n ###\n ###\n")

    def test_str(self):
        """Testing the __str__ literals"""
        self.assertEqual(str(self.my_rect), "[Rectangle] ({}) \
{}/{} - {}/{}".format(10, 1, 1, 3, 2))

    def test_update(self):
        """Testing the update method"""
        self.my_rect.update(12)
        self.assertEqual(str(self.my_rect), "[Rectangle] ({}) \
{}/{} - {}/{}".format(12, 1, 1, 3, 2))

        self.my_rect.update(19, 2, 3, 4, 5, width=1)
        self.assertEqual(str(self.my_rect), "[Rectangle] ({}) \
{}/{} - {}/{}".format(19, 4, 5, 2, 3))

        self.my_rect.update(x=1, height=2, y=3, width=4)
        self.assertEqual(str(self.my_rect), "[Rectangle] ({}) \
{}/{} - {}/{}".format(19, 1, 3, 4, 2))
