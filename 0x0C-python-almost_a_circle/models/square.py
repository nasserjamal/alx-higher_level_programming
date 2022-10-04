#!/usr/bin/python3
"""Module describing a square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Describes a square object"""
    def __init__(self, size, x=0, y=0, id=None):
        """Init method"""
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """String representation of the class"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter. Sets the size of the object"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the values of the rectangle"""
        for key, val in kwargs.items():
            if key == "id":
                self.id = val
            elif key == "size":
                self.size = val
            elif key == "x":
                self.x = val
            elif key == "y":
                self.y = val
        for idx, arg in enumerate(args):
            if idx == 0:
                self.id = arg
            elif idx == 1:
                self.size = arg
            elif idx == 2:
                self.x = arg
            elif idx == 3:
                self.y = arg

    def to_dictionary(self):
        """Converts the object to dictionary"""
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
