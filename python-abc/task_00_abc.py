#!/usr/bin/python3
""""define the Animal class and its subclasses Dog and Cat"""

from abc import ABC, abstractmethod
"""Abstract base class for animals with a method to return their sound"""


class Animal(ABC):
    """Abstract base class for all animals"""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal"""
        pass


class Dog(Animal):
    """Dog class inheriting from Animal"""

    def sound(self):
        """Return the sound made by a dog"""
        return "Bark!"


class Cat(Animal):
    """Cat class inheriting from Animal"""

    def sound(self):
        """Return the sound made by a cat"""
        return "Meow!"
