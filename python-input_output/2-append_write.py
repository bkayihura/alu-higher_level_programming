#!/usr/bin/python3
"""Module that defines a function to append text to a file."""


def append_write(filename="", text=""):
    """Append a string to the end of a text file (UTF8).

    Args:
        filename (str): the path to the file to append to.
        text (str): the text to append.

    Returns:
        int: the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
