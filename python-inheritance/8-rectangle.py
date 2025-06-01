#!/usr/bin/python3
"""Module that defines a class Rectangle."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle:
    """Class that defines a rectangle with width and height."""

    def __init__(self, width, height):
        """Initialize the rectangle with width and height."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
