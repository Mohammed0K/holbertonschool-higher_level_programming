#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


def is_kind_of_class(obj, a_class):
    """Checks if an object is an instance of a class"""
    bool = False
    if isinstance(obj, a_class):
            bool = True
            return bool
