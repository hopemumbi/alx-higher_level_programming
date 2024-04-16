#!/usr/bin/python3
"""Reading a textfile"""


def read_file(filename=""):
    """"reads a text file (UTF8) and prints it to stdout
    Args:
        filename: name of file to be read
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
