#!/usr/bin/python3

ascii = 122
while ascii >= 97:
    c_ascii = ascii
    if c_ascii % 2 == 1:
        c_ascii -= 32
    print("{:c}".format(c_ascii), end="")
    ascii -= 1
