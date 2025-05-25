#!/usr/bin/python3
"""Rectangle class definition"""


class Rectangle:
    
    def __init__(self, width=0, height=0):
        """Initialize a new Rectangle instance."""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """for getting the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """make sure the width is an integer and non-negative."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """to get the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """to make sure the height is an integer and non-negative."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
            