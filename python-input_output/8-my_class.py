#!/usr/bin/python3
"""Module that defines the MyClass class used for JSON serialization."""


class MyClass:
    """A simple class with a name and a number."""

    def __init__(self, name):
        """Initialize a new MyClass instance.

        Args:
            name (str): the name attribute of the instance.
        """
        self.name = name
        self.number = 0

    def __str__(self):
        """Return the string representation of the instance."""
        return "[MyClass] {} - {:d}".format(self.name, self.number)
