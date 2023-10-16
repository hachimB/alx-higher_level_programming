#!/usr/bin/python3
"""Module documentation"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init method"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width getter method"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """width setter method"""
        self.validation("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height getter method"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """height setter method"""
        self.validation("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x getter method"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """x setter method"""
        self.validation("x", value, True)
        self.__x = value

    @property
    def y(self):
        """y getter method"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """y setter method"""
        self.validation("y", value, True)
        self.__y = value

    def validation(self, name, value, boolean=True):
        """validation method"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if boolean and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not boolean and value <= 0:
            raise ValueError("{} must be > 0".format(name))

    def area(self):
        """area method that returns the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """display method"""
        print('\n' * self.y, end="")
        for i in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """__str__ method"""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y,
                                                       self.width, self.height)

    def update(self, *args, **kwargs):
        """update method"""
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:     # kwargs case
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    def to_dictionary(self):
        """to_dictionary method"""
        return ({'x': self.x, 'y': self.y, 'id': self.id,
                 'height': self.height, 'width': self.width})
