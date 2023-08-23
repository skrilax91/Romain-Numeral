# This file contains the functions for converting between Roman numerals and numbers.

# The Roman numerals and their values
ROMAN_NUMERALS = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}


def numeral_to_roman(numeral):
    """Convert a number to a Roman numeral.

    Keyword arguments:
    numeral -- the number to convert

    Returns:
    The Roman numeral represented by the number

    Raises:
    ValueError -- if the number is invalid
    """
    return numeral


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
        if char not in ROMAN_NUMERALS:
            raise ValueError("Invalid Roman numeral")

    # Convert the Roman numeral to a number
    numeral = 0
    for i in range(len(roman)):
        if i > 0 and ROMAN_NUMERALS[roman[i]] > ROMAN_NUMERALS[roman[i - 1]]:
            numeral += ROMAN_NUMERALS[roman[i]] - 2 * ROMAN_NUMERALS[roman[i - 1]]
        else:
            numeral += ROMAN_NUMERALS[roman[i]]

    return numeral
