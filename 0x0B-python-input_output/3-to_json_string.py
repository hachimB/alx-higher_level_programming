#!/usr/bin/python3
"""Module documentation"""
import json


def to_json_string(my_obj):
    """function that returns the JSON representation of an object (string)"""
    json_repr = json.dumps(my_obj)
    return (json_repr)
