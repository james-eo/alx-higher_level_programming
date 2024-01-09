#!/usr/bin/python3
"""Writing in a text file"""


def write_file(filename="", text=""):
    """A functions that writes a string to a text file and returns the number
     of characters written
     Returns:The number of characters written.
    """

    with open(filename, mode='w', encoding="utf-8") as f:
        return f.write(text)
