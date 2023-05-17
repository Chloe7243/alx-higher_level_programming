#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    main_symbols = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    roman_string = roman_string.upper()
    if len(roman_string) > 1 and \
            main_symbols[roman_string[0]] < main_symbols[roman_string[1]]:
        value = main_symbols[roman_string[-1]]
        for i, x in enumerate(reversed(roman_string)):
            if i != 0:
                value -= main_symbols[x]
        return value

    for x in roman_string:
        if x not in main_symbols:
            return 0
        value += main_symbols[x]
    return value
