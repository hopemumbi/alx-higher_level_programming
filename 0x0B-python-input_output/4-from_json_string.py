#!/usr/bin/python3
"""Decode an object represented as a JSON string:"""


def from_json_string(my_str):
    """Decodes an object represented by a JSON string

    Args:
        my_str: Json string

    Returns:
        An object(Python data structure) after decoding
    """
    import json
    return json.loads(my_str)
