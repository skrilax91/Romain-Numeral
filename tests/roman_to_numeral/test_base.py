from numeral import roman_to_numeral


def test_invalid_roman():
    try:
        roman_to_numeral("A")
        assert False
    except ValueError:
        assert True


def test_one():
    assert roman_to_numeral("I") == 1


def test_two():
    assert roman_to_numeral("II") == 2


def test_three():
    assert roman_to_numeral("III") == 3


def test_five():
    assert roman_to_numeral("V") == 5


def test_ten():
    assert roman_to_numeral("X") == 10


def test_fifty():
    assert roman_to_numeral("L") == 50


def test_hundred():
    assert roman_to_numeral("C") == 100


def test_five_hundred():
    assert roman_to_numeral("D") == 500


def test_thousand():
    assert roman_to_numeral("M") == 1000
