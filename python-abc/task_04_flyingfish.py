#!/usr/bin/python3
"""Define the Fish class and its subclass FlyingFish."""


class Fish:
    """A class representing a fish with swimming and habitat methods."""

    def swim(self):
        print("The fish is swimming")

    def habitat(self):
        """Prints the habitat of the fish."""
        print("The fish lives in water")


class Bird:
    def fly(self):
        """Prints a message indicating the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Prints the habitat of the bird."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A class representing a flying fish that can swim and fly."""

    def swim(self):
        """Override the swim method to indicate the flying fish is swimming."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override the fly method to indicate the flying fish is flying."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override the habitat method to indicate the flying fish's unique habitat."""
        print("The flying fish lives both in water and the sky!")
