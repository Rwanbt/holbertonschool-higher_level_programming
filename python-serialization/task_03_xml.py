#!/usr/bin/env python3
"""Module of Serializing and Deserializing with XML"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes a Python dictionary into an XML file"""
    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=False)


def deserialize_from_xml(filename):
    """Deserializes an XML file back into a Python dictionary"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        reconstructed_dict = {}
        for child in root:
            reconstructed_dict[child.tag] = child.text

        return reconstructed_dict

    except Exception:
        return None
