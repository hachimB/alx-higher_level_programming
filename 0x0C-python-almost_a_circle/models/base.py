#!/usr/bin/python3
"""Module documentation"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if not (id is None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if (len(list_dictionaries) == 0 or list_dictionaries is None):
            return "[]"
        return (json.dumps(list_dictionaries))
