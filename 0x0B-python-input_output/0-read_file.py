#!/usr/bin/python3
"""0-read_file.py
"""


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout """

    with open(filename, 'r', encoding="utf-8") as f_obj:
        content = f_obj.read()
    print(content, end="")
