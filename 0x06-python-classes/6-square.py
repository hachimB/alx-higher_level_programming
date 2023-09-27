#!/usr/bin/python3
""" Square class """


class Square:
    """ defines a square """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        self.__size = value
        if not (isinstance(self.__size, int)):
            raise TypeError("size must be an integer")
        if (self.__size < 0):
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if not ((isinstance(self.__position[0], int)) and
                (isinstance(self.__position[1], int))):
        #if not (isinstance(value, tuple) and len(value) == 2 and
         #       isinstance(value[0], int) and isinstance(value[1], int)
          #      and value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        return (self.__size * self.__size)

    def my_print(self):
        if (self.__size == 0):
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
