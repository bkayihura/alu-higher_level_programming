#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        self.__size = size
