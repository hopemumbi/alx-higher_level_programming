#!/usr/bin/python3
"""Writing an Object to a text file, using a JSON representation"""


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation

    Args:
        my_obj: Object to be written using json
        filename: file to write into
    """
    with open(filename, 'w', encoding="utf-8") as f:
        import json
        json.dump(my_obj, f)
