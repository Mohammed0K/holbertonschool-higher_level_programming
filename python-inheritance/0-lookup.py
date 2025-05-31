#!/usr/bin/python3
"""Lookup method resolution order (MRO) in Python classes."""


def lookup(obj):
    """Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        A list of strings representing the names of the object's attributes
        and methods.
    """
    return dir(obj)