#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not type(roman_string) == str and roman_string is None:
        return 0
    s = roman_string.upper()
    roman = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
             'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
    num = 0

    for i in range(len(roman_string)):
        if i != len(roman_string) - 1 and roman[roman_string[i]] < roman[roman_string[i + 1]]:
            num -= roman[roman_string[i]]
        else:
            num += roman[roman_string[i]]
    return num
