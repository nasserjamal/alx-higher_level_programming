#!/usr/bin/python3
"""Module describing a square"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Describes a square object"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
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
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
