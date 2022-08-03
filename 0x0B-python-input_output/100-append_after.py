#!/usr/bin/python3
'''100-append_after.py
'''


def append_after(filename="", search_string="", new_string=""):
    '''inserts new_string to a file, after find containing search_string'''
    with open(filename, "r+") as f_object:
        lines = f_object.readlines()
        changed = []
        for line in range(len(lines)):
            changed.append(lines[line])
            if search_string in lines[line]:
                changed.append(new_string)

        f_object.seek(0)
        f_object.write("".join(changed))
