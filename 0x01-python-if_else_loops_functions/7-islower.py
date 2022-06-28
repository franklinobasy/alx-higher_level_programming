#!/usr/bin/python3

def islower(c):
    ascii = ord(c)
    if (ascii < 97 or ascii > 122):
        return False
    return True
