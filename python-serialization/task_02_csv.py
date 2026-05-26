#!/usr/bin/env python3
"""Module to convert CSV Data to JSON Format"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """Converts data from CSV file to JSON file named data.json"""
    try:
        with open(csv_filename, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data_list = list(csv_reader)

        with open("data.json", "w") as json_file:
            json.dump(data_list, json_file)

        return True

    except Exception:
        return False
