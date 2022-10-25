#!/usr/bin/python3
"""0-class_to_json.py
Defines a Python class-to-JSON function."""


def class_to_json(obj):
    """Return the dictionary repsentation of a simple data structure."""
    return obj.__dict__
