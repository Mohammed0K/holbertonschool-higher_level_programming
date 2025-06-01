#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


def is_same_class(obj, a_class):
    """Checks if an object is exactly an instance of a specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class, False otherwise.
    """
    return type(obj) is a_class
