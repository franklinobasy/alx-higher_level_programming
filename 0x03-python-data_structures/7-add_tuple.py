#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    xa = 0
    xb = 0
    ya = 0
    yb = 0
    if len(tuple_a) < 1:
        pass
    elif len(tuple_a) < 2:
        xa = tuple_a[0]
    else:
        xa = tuple_a[0]
        ya = tuple_a[1]

    if len(tuple_b) < 1:
        pass
    elif len(tuple_b) < 2:
        xb = tuple_b[0]
    else:
        xb = tuple_b[0]
        yb = tuple_b[1]

    i = xa + xb
    j = ya + yb

    return (i, j)
