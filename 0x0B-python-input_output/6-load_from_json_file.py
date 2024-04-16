#!/usr/bin/python3
"""Create an Object from a “JSON file”"""


def load_from_json_file(filename):
    """creates an Object from a “JSON file”

    Args:
        filename: json file to be decoded
    """
    with open(filename, encoding="utf-8") as f:
        import json
        return json.load(f)
