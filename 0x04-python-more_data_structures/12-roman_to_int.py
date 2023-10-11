#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return None
    numerals = {
            'I': 1
            'V': 5
            'X': 10
            'L': 50
            'C': 100
            'D': 500
            'M': 1000
            }
    result = 0
    prev_val = 0

    for ch in roman_string[::-1]:
        value = numerals.get(ch, 0)
        if value < prev_val:
            result -= value
        else:
            result += value
        prev_val = value
    return result
