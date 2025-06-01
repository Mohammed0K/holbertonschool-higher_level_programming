#!/usr/bin/python3
"""Define the Shape class and its subclasses Circle and Rectangle"""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes"""

    @abstractmethod
    def area(self):
        """calculates area of the shape."""
        return 0

    @abstractmethod
    def perimeter(self):
        """calculates perimeter of the shape."""
        return 0


class Circle(Shape):
    """Class Circle"""
    __radius = 0

    def __init__(self, radius=0):
        """initializes Circle with a radius"""
        self.radius = radius

    @property
    def radius(self):
        """Gets private value of radius"""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Sets and validates value of private attribute radius"""
        if value < 0:
            value = abs(value)

        self.__radius = value

    def area(self):
        """abstract method of area"""
        area = math.pi * self.radius * self.radius
        print("Area: {:0.1f}".format(area))

        return area

    def perimeter(self):
        """function to calculate perimeter of Circle"""
        perimeter = 2 * math.pi * self.radius
        print("Perimeter: {:0.1f}".format(perimeter))

        return perimeter


class Rectangle(Shape):
    """Class Rectangle"""
    __width = 0
    __height = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter for private attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """"Sets and validates value of private attribute width"""
        self.__width = value

    @property
    def height(self):
        """Getter for private attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets and validates value of private attribute height"""
        self.__height = value

    def area(self):
        """reimplements abstract method of area"""
        area = self.width * self.height
        print("Area: {:0.1f}".format(area))

        return area

    def perimeter(self) -> float:
        """reimplements abstract method of perimeter"""
        perimeter = 2 * (self.width + self.height)
        print("Perimeter: {:0.1f}".format(perimeter))

        return perimeter


def shape_info(shape: Shape):
    """Function to print area and perimeter of a shape"""
    area = shape.area()
    perimeter = shape.perimeter()

    return {'area': area, 'perimeter': perimeter}
