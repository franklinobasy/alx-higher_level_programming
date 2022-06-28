#!/usr/bin/python3

i = 0
while i <= 99:
    print(f"0{i}" if i < 10 else f"{i}", end=", " if i < 99 else "\n")
    i += 1
