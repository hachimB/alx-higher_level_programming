#!/usr/bin/python3
"""class documentation"""


class Rectangle:
    """class of Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if (value < 0):
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if (value < 0):
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.width * self.height)

    def perimeter(self):
        if (self.width == 0 or self.height == 0):
            perim = 0
        else:
            perim = (self.width + self.height) * 2
        return (perim)

    def __str__(self):
        s = ""
        if (self.width != 0 and self.height != 0):
            s = "\n".join("#" * self.width for i in range(self.height))
        return (s)
