# This file contains the functions for converting between Roman numerals and numbers.

# The Roman numerals and their values
ROMAN = ["I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"]
NUMERALS = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]


def numeral_to_roman(numeral):
    """Convert a number to a Roman numeral.

    Keyword arguments:
    numeral -- the number to convert

    Returns:
    The Roman numeral represented by the number

    Raises:
    ValueError -- if the number is invalid
    """

    # Test for invalid arguments
    if not isinstance(numeral, int):
        raise ValueError("Invalid argument")

    # Test for invalid numbers
    if numeral < 1 or numeral > 3999:
        raise ValueError("Invalid number")

    # Convert the number to a Roman numeral
    roman = ""
    for i in range(len(NUMERALS) - 1, -1, -1):
        while numeral >= NUMERALS[i]:
            roman += ROMAN[i]
            numeral -= NUMERALS[i]

    return roman


def roman_to_numeral(roman):
    """Convert a Roman numeral to a number.

    Keyword arguments:
    roman -- the Roman numeral to convert

    Returns:
    The number represented by the Roman numeral

    Raises:
    ValueError -- if the Roman numeral is invalid
    """

    # Test for invalid Roman numerals
    for char in roman:
        if char not in ROMAN:
            raise ValueError("Invalid Roman numeral")

    # Convert the Roman numeral to a number
    numeral = 0
    for i in range(len(roman)):
        if i > 0 and NUMERALS[ROMAN.index(roman[i])] > NUMERALS[ROMAN.index(roman[i - 1])]:
            numeral += NUMERALS[ROMAN.index(roman[i])] - 2 * NUMERALS[ROMAN.index(roman[i - 1])]
        else:
            numeral += NUMERALS[ROMAN.index(roman[i])]

    return numeral
