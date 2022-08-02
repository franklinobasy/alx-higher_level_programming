#!/usr/bin/python3
'''7-add_item.py
    a script that adds all arguments to a Python list,
    and then save them to a file
'''

from os import path
import sys


if __name__ == "__main__":
    argv = sys.argv[1:]

    save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
    load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

    file_path = "add_item.json"
    if path.exists(file_path):
        list_obj = load_from_json_file(file_path)
    else:
        list_obj = list()
    
    save_to_json_file(list_obj + argv, file_path)
    print(end="")
