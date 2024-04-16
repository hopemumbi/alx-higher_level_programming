#!/usr/bin/python3
"""Write a string to a textfile"""


def write_file(filename="", text=""):
    """function that writes a string to a text file (UTF8)

    Args:
        filename: Name of textfile.
        test: String to be written

    Return:
        The number of characters written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
