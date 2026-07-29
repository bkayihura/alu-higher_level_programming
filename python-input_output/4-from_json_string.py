#!/usr/bin/python3
"""Module that defines a function to convert a JSON string to an object."""
import json


def from_json_string(my_str):
    """Return an object represented by a JSON string.

    Args:
        my_str (str): the JSON string to deserialize.

    Returns:
        The Python data structure represented by my_str.
    """
    return json.loads(my_str)
