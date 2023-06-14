#!/usr/bin/python3
import json
""" returns the JSON representation of an object (string) """


def from_json_string(my_obj):
    """ returns the JSON representation of an object (string) """
    return json.loads(my_obj)
