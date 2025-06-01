#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


def inherits_from(obj, a_class):
    """" Return: True if obj is an instance of a class that"""""
    return isinstance(obj, a_class) and type(obj) is not a_class
