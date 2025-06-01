#!/usr/bin/python3
"""Define the Shape class and its subclasses Circle and Rectangle"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""
    @abstractmethod
    def area(self):
        """Method to calculate the area of the shape"""
        pass

    @abstractmethod
    def perimeter(self):
        """Method to calculate the perimeter of the shape"""
        pass


class Circle(Shape):
    """Class representing a Circle, inheriting from Shape."""

    def __init__(self, radius):
        """Initialize the Circle with a radius"""
        self.radius = radius

    def area(self):
        """Calculate the area of the Circle"""
        return math.pi * (self.radius * self.radius)

    def perimeter(self):
        """Calculate the perimeter (circumference) of the Circle"""
        return math.pi * 2 * self.radius


class Rectangle(Shape):
    """Class representing a Rectangle, inheriting from Shape."""

    def __init__(self, width, height):
        """Initialize the Rectangle with width and height"""
        self.width = width
        self.height = height

    def area(self):
        """Calculate the area of the Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate the perimeter of the Rectangle"""
        return 2 * (self.width + self.height)


def shape_info(obj):
    """Function to print the area and perimeter of a shape object."""
    print("Area:", obj.area())
    print("Perimeter:", obj.perimeter())
