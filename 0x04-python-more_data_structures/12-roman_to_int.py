#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    main_symbols = \
        {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    roman_string = roman_string.upper()

    for i, x in enumerate(roman_string):
        if x not in main_symbols:
            return 0
        if len(roman_string) > 1 and \
                main_symbols[x]  < main_symbols[roman_string[-1]]:
            value += (main_symbols[roman_string[-1]] - main_symbols[x])
            return value
        value += main_symbols[x]
    return value

roman_number = "X"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "VII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "IX"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "LXXXVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "DCCVII"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "l"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))

roman_number = "liv"
print("{} = {}".format(roman_number, roman_to_int(roman_number)))
