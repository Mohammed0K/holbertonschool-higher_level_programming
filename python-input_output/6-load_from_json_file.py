#!/usr/bin/python3
"""Defines a function that returns the JSON
 representation of an object (string)."""
import json


def load_from_json_file(filename):
    """Creates an Object from a “JSON file”."""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
