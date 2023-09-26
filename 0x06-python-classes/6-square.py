#!/usr/bin/python3
""" Square class """


class Square:
    """ defines a square """
    def __init__(self, size=0, position=(0, 0)):
        self._size = size
        self._position = position

    @property
    def size(self):
        return (self._size)

    @size.setter
    def size(self, value):
        self._size = value
        if not (isinstance(self._size, int)):
            raise TypeError("size must be an integer")
        if (self._size < 0):
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return (self._position)

    @position.setter
    def position(self, value):
        if not (((isinstance(self._position[0], int)) and
                 (isinstance(self._position[1], int)))):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

    def area(self):
        return (self._size * self._size)

    def my_print(self):
        if (self._size == 0):
            print()
        if (self._position[1] > 0):
            print()
        else:
            for i in range(self._size):
                for j in range(self._size):
                    print("#", end="")
                print()
