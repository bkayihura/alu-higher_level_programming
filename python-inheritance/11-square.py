#!/usr/bin/python3
"""Module that defines a Square class with its own string repr."""
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

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(
            self._Rectangle__width, self._Rectangle__height)
