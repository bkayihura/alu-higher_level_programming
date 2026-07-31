#!/usr/bin/python3
"""Module that defines a function to convert a class instance to a dict."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON
    serialization.

    Args:
        obj: an instance of a class whose attributes are all
            serializable (list, dict, str, int, bool).

    Returns:
        dict: the dictionary representation of obj's attributes.
    """
    return obj.__dict__
