#!/usr/bin/python3
"""Defines a function that adds two integers."""


def add_integer(a, b=98):
    """Adds two integers.
    Args:
        a: first integer
        b: second integer, defaults to 98
    Raises:
        TypeError: if either a or b is not an integer
    Returns:
        The sum of a and b, rounded down to the nearest integer.
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return (a + b)
