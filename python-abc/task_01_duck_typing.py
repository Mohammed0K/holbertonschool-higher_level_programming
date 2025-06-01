#!/usr/bin/python3
"""Defines Shape, Circle, Rectangle, and shape_info for duck typing exercise."""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""
    @abstractmethod
    def area(self):
        """Calculate area."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate perimeter."""
        pass


class Circle(Shape):
    """Circle shape with radius."""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Return area of the circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return perimeter of the circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle shape with width and height."""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Return area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of the rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of a shape."""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
