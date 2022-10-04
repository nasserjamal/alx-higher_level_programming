#!/usr/bin/python3
"""Rectangle module"""


from array import array
from models.base import Base


class Rectangle(Base):
    """Contains defination of the Recatngle object"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initial method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """String conversion"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
self.__y, self.__width, self.__height)

    # Width Getter and setter
    @property
    def width(self):
        """Width getter. Returns the width variable"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter and validator. Validates width before setting it"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # Height Getter and setter
    @property
    def height(self):
        """Height getter. Returns the __height variable"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter. Validates before setting it"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # x Getter and setter
    @property
    def x(self):
        """X offset getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """X offset validate and set"""
        if (type(value) is not int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # y Getter and setter
    @property
    def y(self):
        """Y offset getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y offset setter and validator"""
        if (type(value) is not int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate and Return the area of shape"""
        return self.__height * self.__width

    def display(self):
        """Display the shape using #"""
        [print("") for pos_y in range(0, self.__y)]
        for row in range(0, self.__height):
            [print(" ", end="") for pos_x in range(0, self.__x)]
            [print("#", end="") for col in range(0, self.__width)]
            print("")

    def update(self, *args, **kwargs):
        """Update vallues of the shape"""
        for key, val in kwargs.items():
            if (f"_Rectangle__{key}" in self.__dict__):
                if key == "id":
                    self.id = val
                elif key == "width":
                    self.width = val
                elif key == "height":
                    self.height = val
                elif key == "x":
                    self.x = val
                elif key == "y":
                    self.y = val
        for idx, arg in enumerate(args):
            if idx == 0:
                self.id = arg
            elif idx == 1:
                self.width = arg
            elif idx == 2:
                self.height = arg
            elif idx == 3:
                self.x = arg
            elif idx == 4:
                self.y = arg

    def to_dictionary(self):
        """Return the dictionary description of the shape"""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
