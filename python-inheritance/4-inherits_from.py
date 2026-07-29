#!/usr/bin/python3
"""Module that defines a function checking strict inheritance."""


def inherits_from(obj, a_class):
    """Return True if obj is an instance of a class that inherited
    (directly or indirectly) from a_class, but is not a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) != a_class
