#!/usr/bin/python3
"""Module documentation"""
import json


def from_json_string(my_str):
    """function that returns an object
(Python data structure) represented by a JSON string"""
    jsn_to_obj = json.loads(my_str)
    return (jsn_to_obj)
