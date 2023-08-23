from numeral import roman_to_numeral


def test_multiple_of_ten():
    assert roman_to_numeral("X") == 10
    assert roman_to_numeral("XX") == 20
    assert roman_to_numeral("XXX") == 30
    assert roman_to_numeral("XL") == 40
    assert roman_to_numeral("LX") == 60
    assert roman_to_numeral("LXX") == 70
    assert roman_to_numeral("LXXX") == 80
    assert roman_to_numeral("XC") == 90
    assert roman_to_numeral("CX") == 110
    assert roman_to_numeral("CXX") == 120
    assert roman_to_numeral("CXXX") == 130
    assert roman_to_numeral("CXL") == 140
    assert roman_to_numeral("CLX") == 160
    assert roman_to_numeral("CLXX") == 170
    assert roman_to_numeral("CLXXX") == 180
    assert roman_to_numeral("CXC") == 190


def test_multiple_of_hundred():
    assert roman_to_numeral("C") == 100
    assert roman_to_numeral("CC") == 200
    assert roman_to_numeral("CCC") == 300
    assert roman_to_numeral("CD") == 400
    assert roman_to_numeral("DC") == 600
    assert roman_to_numeral("DCC") == 700
    assert roman_to_numeral("DCCC") == 800
    assert roman_to_numeral("CM") == 900
    assert roman_to_numeral("MC") == 1100


def test_multiple_of_thousand():
    assert roman_to_numeral("M") == 1000
    assert roman_to_numeral("MM") == 2000


def test_multiple_of_five():
    assert roman_to_numeral("V") == 5
    assert roman_to_numeral("VV") == 10
    assert roman_to_numeral("VVV") == 15


# Test random complexe numbers
def test_complex_number():
    assert roman_to_numeral("MCMXCIX") == 1999
    assert roman_to_numeral("MMXIX") == 2019
    assert roman_to_numeral("DCCXXXVIII") == 738

