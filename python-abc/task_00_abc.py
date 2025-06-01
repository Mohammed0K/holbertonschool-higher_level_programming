#!/usr/bin/env python3
""""define the Animal class and its subclasses abc"""


from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for all animals"""

    @abstractmethod
    def sound(self) -> str:
        """Return the sound made by the animal"""
        pass
