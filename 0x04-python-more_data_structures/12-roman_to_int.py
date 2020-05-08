#!/usr/bin/python3
def roman_to_int(roman_string):
    rom_n = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    prev = 0
    roman_sum = 0
    if type(roman_string) is str:
        for n in roman_string:
            if rom_n[n] > prev:
                roman_sum -= prev
            else:
                roman_sum += prev
            prev = rom_n[n]
        roman_sum += prev
    return roman_sum
