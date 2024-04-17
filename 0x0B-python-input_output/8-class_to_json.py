#!/usr/bin/python3
def class_to_json(obj):
    """
    Return a dictionary description for JSON serialization of an object.

    Args:
        obj: An instance of a Class.

    Returns:
        A dictionary representing the JSON serialization of the object.
        The dictionary contains all serializable attributes of the object,
        including lists, dictionaries, strings, integers, and booleans.
    """
    return obj.__dict__
