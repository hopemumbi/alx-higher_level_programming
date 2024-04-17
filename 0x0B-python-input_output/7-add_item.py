#!/usr/bin/python3
"""
Script to add arguments to a JSON file.

This script reads command-line arguments from stdin, skips the first argument,
and adds the remaining arguments to a JSON file named "add_item.json".
If the file doesn't exist, it will be created.

Usage:
    ./script.py arg1 arg2 ...

Args:
    arg1, arg2, ...: Command-line arguments to be added to the JSON file.
"""

import sys

# Dynamically import functions from external modules
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

# Define the filename for the JSON file
filename = "add_item.json"

# Load existing data from the JSON file, or initialize an empty list
try:
    my_list = load_from_json_file(filename)
except FileNotFoundError:
    my_list = []

# Read command-line arguments from stdin, skipping the first argument
arguments = sys.argv[1:]
for arg in arguments:
    my_list.append(arg)

# Save the updated list to the JSON file
save_to_json_file(my_list, filename)
