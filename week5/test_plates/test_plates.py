from plates import is_valid

def test_length():
    assert is_valid("") == False
    assert is_valid("o") == False
    assert is_valid("woooooo123") == False


def test_start():
    assert is_valid("ABC12") == True
    assert is_valid("12") == False
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("AA") == True
    assert is_valid("12abc") == False
    assert is_valid("o23as") == False
    assert is_valid("P2P3") == False


def test_numbers():
    assert is_valid("CS50P") == False
    assert is_valid("nu89pp") == False
    assert is_valid("CS05") == False


def test_special_char():
    assert is_valid("CS:50") == False
    assert is_valid("PL,A5") == False
    assert is_valid("CS 50") == False
    assert is_valid("CS. 50") == False
    assert is_valid("???") == False


def test_valid():
    assert is_valid("CS50") == True
    assert is_valid("NXR187") == True


