#!/usr/bin/python3
"""Module documentation"""
import json


def class_to_json(obj):
    """class _to_json function"""
    dict_desc = json.dumps(obj.__dict__)
    return (dict_desc)
