#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


def print_sorted(self):
    """Prints the list, but sorted (ascending sort)."""
    print(sorted(self))


class MyList(list):
    """Class that inherits from list and adds a method to print sorted."""

    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
