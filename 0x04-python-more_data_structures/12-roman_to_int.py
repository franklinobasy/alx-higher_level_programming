#!/usr/bin/python3

ROMAN = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10,
         "XL": 40, "L": 50, "XC": 90, "C": 100, "CD": 400,
         "D": 500, "CM": 900, "M": 1000}


def roman_to_int(roman_string):
    result = 0
    if not isinstance(roman_string, str):
        return result

    r_numeral = ROMAN.keys()
    n = len(roman_string)
    i = 0
    while i < n:
        check1 = roman_string[i:i+2]
        check2 = roman_string[i]
        if check1 in r_numeral:
            result += ROMAN.get(check1)
            i += 2
        elif check2 in r_numeral:
            result += ROMAN.get(check2)
            i += 1

    return result
