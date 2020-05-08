#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_num = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    prev = 0
    roman_sum = 0
    if type(roman_string) is str:
        for n in roman_string:        
            if roman_num[n] is > prev:
                roman_sum -= prev
            else:
                roman_sum += prev
            prev = roman_num[n]
        roman_sum += prev
    return roman_sum
