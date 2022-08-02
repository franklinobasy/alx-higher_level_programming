#!/usr/bin/python3
''' 4-append_write.py
'''


def append_write(filename="", text=""):
    ''' appends a string at the end of a text file '''

    with open(filename, 'a', encoding="utf-8") as f_obj:
        return f_obj.write(text)
