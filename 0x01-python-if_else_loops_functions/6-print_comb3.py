#!/usr/bin/python3

i = 0
j = 0

while i < 10:
    j = 0
    while j < 10:
        if (i != j and i < j):
            print("{0:d}{1:d}".format(i, j), end="")
            if (i >= 8 and j >= 9):
                print()
            else:
                print(end=", ")
        j += 1
    i += 1
