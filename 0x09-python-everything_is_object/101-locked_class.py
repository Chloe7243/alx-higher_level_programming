#!/usr/bin/python3
"""Defines a class: LockedClass"""


class LockedClass:
    """A class that only allows first_name attribute"""
    __slots__ = ["first_name"]
