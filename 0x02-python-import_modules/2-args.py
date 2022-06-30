#!/usr/bin/python3
import sys

if __name__ == '__main__':
    argv = sys.argv
    n = len(argv)
    if n == 1:
        print(f"{n-1:d} arguments.")
    else:
        print(f"{n-1:d} argument:" if n == 2 else f"{n-1:d} arguments:")
        for i in range(1, n):
            print(f"{i:d}: {argv[i]:s}")
