#!/usr/bin/python3
"""Appending a string at the end of a text file"""


def append_write(filename="", text=""):
    """function that appends a string at the end of a text file (UTF8)

    Args:
        filename: The name of the textfile
        text: Text to be appended

    Return:
        The number of characters printed
    """
    with open(filename, mode='a', encoding='utf-8') as f:
        return f.write(text)
