#!/usr/bin/python3
"""Module that defines a class Rectangle."""


class Rectangle:
    """Class that defines a rectangle with width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
