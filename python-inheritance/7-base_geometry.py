#!/usr/bin/python3
"""Module that defines the BaseGeometry class with validation."""


class BaseGeometry:
    """Base class for geometry-related classes."""

    def area(self):
        """Raise an exception since area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer.

        Args:
            name (str): the name of the attribute being validated.
            value (int): the value to validate.

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is not greater than 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
