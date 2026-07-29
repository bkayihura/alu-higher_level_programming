#!/usr/bin/python3
"""Module that defines a function to read and print a text file."""


def read_file(filename=""):
    """Read a text file (UTF8) and print its content to stdout.

    Args:
        filename (str): the path to the file to read.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
