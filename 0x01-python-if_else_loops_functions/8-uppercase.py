#!/usr/bin/python3

def uppercase(str):
    for c in str:
        ascii = ord(c)
        ascii = ascii - 32
        print("{0:c}".format(ascii), end="")
    print()