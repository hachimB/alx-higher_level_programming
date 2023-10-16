#!/usr/bin/python3
"""Module documentation"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init method"""
        if not (id is None):
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string method"""
        if (len(list_dictionaries) == 0 or list_dictionaries is None):
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file method"""
        if list_objs is None:
            list_objs = []
        else:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w",
                  encoding="utf8") as file:
            file.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """from_json_string method"""
        if (not json_string or json_string is None):
            return []
        return json.loads(json_string)
