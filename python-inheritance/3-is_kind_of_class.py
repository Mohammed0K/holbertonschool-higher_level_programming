#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of, or if it is an instance of a class
    that inherited from, the specified class.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        True if obj is an instance of a_class or an inherited class, False otherwise.
    """
    return isinstance(obj, a_class)
