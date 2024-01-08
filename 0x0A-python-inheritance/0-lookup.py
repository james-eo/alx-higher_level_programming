#!/usr/bin/python3
"""Defines an object attribute lookup function."""


def lookup(obj):
    """Return a list of available attributes for an object."""
    return (dir(obj))
