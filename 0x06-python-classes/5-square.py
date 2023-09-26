#!/usr/bin/python3
""" Square class """


class Square:
    """ defines a square """
    def __init__(self, size=0):
        self._size = size

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

    def area(self):
        return (self._size * self._size)

    def my_print(self):
        if (self._size == 0):
            print()
        else:
            for i in range(self._size):
                for j in range(self._size):
                    print("#", end="")
                print()
