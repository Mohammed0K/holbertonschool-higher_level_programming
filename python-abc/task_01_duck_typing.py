#!/usr/bin/python3
""" Module for the Shape abstract class and subclasses """

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Shape class"""
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Circle(Shape):
    """Circle Class"""

    def __init__(self, radius=0):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle Class"""

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


def shape_info(shape):
    """shape information function"""
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
