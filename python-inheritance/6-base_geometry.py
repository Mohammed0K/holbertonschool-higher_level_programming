#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


class BaseGeometry:
    """Class that defines a base geometry."""

    def area(self):
        """Calculates the area of the geometry.

        Raises:
            Exception: If the area is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is an integer greater than 0.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
