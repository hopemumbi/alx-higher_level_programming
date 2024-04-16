#!/usr/bin/python3
"""The json representation of an object(string)"""


def to_json_string(my_obj):
    """function that returns the JSON representation of an object

    Args:
        my_obj :

    Returns:
        The JSON representation of an object (string)
    """
    import json
    return json.dumps(my_obj)
