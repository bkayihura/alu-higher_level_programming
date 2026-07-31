#!/usr/bin/python3
"""Defines a function that returns a copy of a list."""


def copy_list(lst):
    """Return a shallow copy of the given list.

    Args:
        lst (list): The list to copy.

    Returns:
        list: A new list with the same elements as lst.
    """
    return lst[:]
