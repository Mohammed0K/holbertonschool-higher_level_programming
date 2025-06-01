#!/usr/bin/python3
"""Define the SSwimMixinhape class and its subclass flyMixin and Dragon."""


class SwimMixin:
    """Mixin class to add swimming behavior."""

    def swim(self):
        """Method to simulate swimming."""
        print("The creature swims!")


class FlyMixin:
    """Mixin class to add flying behavior."""

    def fly(self):
        """Method to simulate flying."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Class representing a Dragon that can swim and fly."""

    def roar(self):
        """Method to simulate a dragon's roar."""
        print("The dragon roars!")
