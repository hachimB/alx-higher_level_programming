#!/usr/bin/pyton3
"""Module documentation"""


def is_kind_of_class(obj, a_class):
    """function that returns True if the object is an instance
of, or if the object is an instance of a class that inherited
,the specified class ; otherwise False."""
    return (isinstance(obj, a_class))
