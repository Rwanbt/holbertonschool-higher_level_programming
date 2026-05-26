#!/usr/bin/env python3
"""
This module provides functions to serialize a Python dictionary
to a JSON file and deserialize a JSON file back to a Python dictionary.
"""

import pickle


class CustomObject:
    """CustomObject class"""

    def __init__(self, name, age, is_student):
        """Init method"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display method"""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """Serialize method"""
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize method"""
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)
        except Exception:
            return None
