from numeral import numeral_to_roman


def test_invalid_numeral():
    try:
        numeral_to_roman(-1)
        numeral_to_roman(0)
        numeral_to_roman(4000)
        numeral_to_roman(3.14)
        numeral_to_roman("A")
        assert False
    except ValueError:
        assert True


def test_one():
    assert numeral_to_roman(1) == "I"


def test_two():
    assert numeral_to_roman(2) == "II"


def test_three():
    assert numeral_to_roman(3) == "III"


def test_five():
    assert numeral_to_roman(5) == "V"


def test_ten():
    assert numeral_to_roman(10) == "X"


def test_fifty():
    assert numeral_to_roman(50) == "L"


def test_hundred():
    assert numeral_to_roman(100) == "C"


def test_five_hundred():
    assert numeral_to_roman(500) == "D"


def test_thousand():
    assert numeral_to_roman(1000) == "M"