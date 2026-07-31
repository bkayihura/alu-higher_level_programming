#!/usr/bin/python3
"""Module that defines a Student class with save/reload support."""


class Student:
    """Represents a student with a first name, last name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the student's first name.
            last_name (str): the student's last name.
            age (int): the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return a dictionary representation of the Student instance.

        Args:
            attrs (list): optional list of attribute names to include.
                If not a list of strings, all attributes are included.

        Returns:
            dict: the filtered or full dictionary of attributes.
        """
        if isinstance(attrs, list) and all(
                isinstance(a, str) for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dict.

        Args:
            json (dict): a dictionary of attribute names and values.
        """
        for key, value in json.items():
            setattr(self, key, value)
