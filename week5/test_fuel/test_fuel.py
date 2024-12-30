import pytest
from fuel import convert, gauge


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        convert("4/0")


def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/meow")
    with pytest.raises(ValueError):
        convert("tutel")
    with pytest.raises(ValueError):
        convert("5")
    with pytest.raises(ValueError):
        convert("1/cat")
    with pytest.raises(ValueError):
        convert("cat/5")


def test_convert():
    assert convert("3/4") == 75
    assert convert("0/5") == 0
    assert convert("4/4") == 100



def test_gauge():
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(33) == "33%"


def test_both():
    assert gauge(convert("4/5")) == "80%"
    assert gauge(convert("0/1")) == "E"
    assert gauge(convert("999/1000")) == "F"

