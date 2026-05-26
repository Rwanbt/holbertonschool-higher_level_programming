#!/usr/bin/env python3
"""
This module provide functions to serialize a python dictionary
to a json file and deserialize a json file back to a python dictionary.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Serialize a python dictionary and saves it to json file.

    Args:
        data (dict): The python dictionary to serialize.
        filename (str): The filename of the output json file.
            If the file exists, it will be replaced.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Loads and deserializes data from a json file back into a python dictionary.

    Args:
        filename (str): The filename of the input json file.

    Returns:
        dict: The deserialized python dictionary from the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
