#!/usr/bin/python3
"""Module that defines a function checking exact class match."""


def is_same_class(obj, a_class):
    """Return True if obj is exactly an instance of a_class."""
    return type(obj) == a_class
