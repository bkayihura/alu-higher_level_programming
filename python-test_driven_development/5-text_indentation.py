#!/usr/bin/python3
"""Module for printing text with indentation after . ? and :
"""


def text_indentation(text):
    """Prints text with 2 new lines after each ., ? and :.

    Args:
        text: the text to print (string).

    Raises:
        TypeError: if text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in ".?:":
            result += "\n\n"
    lines = result.split("\n")
    while lines and lines[-1] == "":
        lines.pop()
    for i, line in enumerate(lines):
        if i == len(lines) - 1:
            print(line.strip(), end="")
        else:
            print(line.strip())
