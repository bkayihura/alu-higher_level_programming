#!/usr/bin/python3
"""Module that defines a Square class inheriting from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a square, based on the Rectangle class."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): the size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
