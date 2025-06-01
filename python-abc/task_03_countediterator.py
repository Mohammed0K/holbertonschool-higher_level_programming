#!/usr/bin/python3
"""Define the CountedIterator class that counts items iterated over."""


class CountedIterator:
    """An iterator that counts the number of items iterated over."""

    def __init__(self, iterable):
        """Initialize the iterator with an iterable."""
        self.iterator = iter(iterable)
        self.count = 0

    def __iter__(self):
        """Return the iterator object itself."""
        return self

    def __next__(self):
        """Return the next item from the iterator and increment the count."""
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """Return the number of items iterated over."""
        return self.count
