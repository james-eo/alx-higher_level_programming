#!/usr/bin/python3
"""Defines a class that is locked"""


class LockedClass:
    """Prevents a user from dynamically creating
    a new instance attributes except if the new
    instant attribute is called first_name."""

    __slots__ = ("first_name",)
