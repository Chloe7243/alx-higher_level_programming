#!/usr/bin/python3
class LockedClass:
    __slots__ = ["first_name"]
    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)
