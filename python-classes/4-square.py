#!/usr/bin/python3
"""Module that defines a class Square."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """ Initialize a square with a given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """ Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """ Set the size of the square."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate the area of the square."""
        return self.__size ** 2
