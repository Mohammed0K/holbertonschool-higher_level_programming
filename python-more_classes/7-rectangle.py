#!/usr/bin/python3
"""Module for Rectangle class."""


class Rectangle:
    """A class that defines a rectangle by its width and height."""

    number_of_instances = 0

    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """function to initialize a rectangle with width and height."""
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
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """for getting the current width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """for setting a new width for the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """for get the current height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """for setting a new height for the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Calculate and return the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """for printing the rectangle with the specified symbol."""
        if self.__width == 0 or self.__height == 0:
            return ""
        symbol = str(self.print_symbol)
        return "\n".join(symbol * self.__width for _ in range(self.__height))

    def __repr__(self):
        """Return a string representation for debugging."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Handle the deletion of a Rectangle instance."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
