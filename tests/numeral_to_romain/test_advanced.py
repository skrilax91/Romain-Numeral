from numeral import numeral_to_roman


def test_multiple_of_ten():
    assert numeral_to_roman(10) == "X"
    assert numeral_to_roman(20) == "XX"
    assert numeral_to_roman(30) == "XXX"
    assert numeral_to_roman(40) == "XL"
    assert numeral_to_roman(60) == "LX"
    assert numeral_to_roman(70) == "LXX"
    assert numeral_to_roman(80) == "LXXX"
    assert numeral_to_roman(90) == "XC"
    assert numeral_to_roman(110) == "CX"
    assert numeral_to_roman(120) == "CXX"
    assert numeral_to_roman(130) == "CXXX"
    assert numeral_to_roman(140) == "CXL"
    assert numeral_to_roman(160) == "CLX"
    assert numeral_to_roman(170) == "CLXX"
    assert numeral_to_roman(180) == "CLXXX"
    assert numeral_to_roman(190) == "CXC"


def test_multiple_of_hundred():
    assert numeral_to_roman(100) == "C"
    assert numeral_to_roman(200) == "CC"
    assert numeral_to_roman(300) == "CCC"
    assert numeral_to_roman(400) == "CD"
    assert numeral_to_roman(600) == "DC"
    assert numeral_to_roman(700) == "DCC"
    assert numeral_to_roman(800) == "DCCC"
    assert numeral_to_roman(900) == "CM"
    assert numeral_to_roman(1100) == "MC"


def test_multiple_of_thousand():
    assert numeral_to_roman(1000) == "M"
    assert numeral_to_roman(2000) == "MM"


def test_multiple_of_five():
    assert numeral_to_roman(5) == "V"
    assert numeral_to_roman(10) == "X"
    assert numeral_to_roman(15) == "XV"


# Test random complexe numbers
def test_complex_number():
    assert numeral_to_roman(1999) == "MCMXCIX"
    assert numeral_to_roman(2019) == "MMXIX"
    assert numeral_to_roman(738) == "DCCXXXVIII"

