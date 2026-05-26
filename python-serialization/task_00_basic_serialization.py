#!/usr/bin/env python3
"""
This module give a function for serialization of file.
"""

import json


def serialize_and_save_to_file(data, filename):
    """
    Load and deserialize data of json file in python dictionary

    Args:
        filename (str): The name of input json file.

    Return:
        dict: The python dictionary deserialize to file
    """
    with open(filename, "w", encoding="utf8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """
    Load and deserialize data of json file in python dictionary

    Args:
        filename (str): The name of json file input.

    Return:
        dict: The python dictionary deserialize to file
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
