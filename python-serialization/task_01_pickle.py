#!/usr/bin/env python3
"""
This module provides functions to serialize a Python dictionary
to a JSON file and deserialize a JSON file back to a Python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary and saves it to a JSON file.

    Args:
        data (dict): The Python dictionary to serialize.
        filename (str): The filename of the output JSON file.
            If the file exists, it will be replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a JSON file back into a Python dictionary.

    Args:
        filename (str): The filename of the input JSON file.

    Returns:
        dict: The deserialized Python dictionary from the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
