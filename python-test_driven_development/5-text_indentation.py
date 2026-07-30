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
    for i, char in enumerate(text):
        result += char
        if char in ".?:" and (i + 1 == len(text) or text[i + 1] == " "):
            result += "\n\n"
    lines = result.split("\n")
    while lines and lines[-1] == "":
        lines.pop()
    for line in lines:
        print(line.strip())
