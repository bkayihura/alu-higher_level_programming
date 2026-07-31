#!/usr/bin/python3
"""Defines a function that returns a comma-separated magic string."""


def magic_string(lst=[]):
    """Append 'BestSchool' to lst and return items joined by ', '.

    Args:
        lst (list): The list to append to and join.

    Returns:
        str: The elements of lst joined by ", ".
    """
    lst += ["BestSchool"]
    return ", ".join(lst)
