#!/usr/bin/python3

def uppercase(str):
    special_chars = " ,-_@^*&%$!"
    for c in str:
        ascii = ord(c)
        if c not in special_chars:
            if ascii >= 97:
                ascii = ascii - 32
        print("{0:c}".format(ascii), end="")
    print()
