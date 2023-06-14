#!/usr/bin/python3
"""Module that defines a is_same_class function"""


def is_same_class(obj, a_class):
    """is obj an instance of a_class?

        Return:
            True or False
    """
    if a_class is object:
        return False
    return isinstance(obj, a_class)
