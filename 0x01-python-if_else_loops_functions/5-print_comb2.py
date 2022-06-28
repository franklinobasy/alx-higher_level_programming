#!/usr/bin/python3

i = 0
while i <= 99:

    print("0{0:d}".format(i) if i < 10 else "{0:d}".format(i),
          end=", " if i < 99 else "\n")

    i += 1
