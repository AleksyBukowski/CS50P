from working import convert

from pytest import raises


def test_with_mins():
    assert convert("3:00 AM to 5:15 PM") == "03:00 to 17:15"
    assert convert("4:00 AM to 9:30 AM") == "04:00 to 09:30"
    assert convert("11:00 PM to 6:20 AM") == "23:00 to 06:20"
    assert convert("1:00 PM to 7:00 AM") == "13:00 to 07:00"



def test_without_mins():
    assert convert("5 AM to 6 PM") == "05:00 to 18:00"
    assert convert("3 AM to 5:15 PM") == "03:00 to 17:15"
    assert convert("5:45 AM to 5 PM") == "05:45 to 17:00"


def test_invalid_format():
    with raises(ValueError):
        convert("14 AM to 6 PM")
    with raises(ValueError):
        convert("4 AM to 16 PM")
    with raises(ValueError):
        convert("11:69 AM to 10 PM")
    with raises(ValueError):
        convert("11:15 AM to 3:333 PM")
    with raises(ValueError):
        convert("-1:1 AM to 6 PM")
    with raises(ValueError):
        convert("09:00 AM - 17:00 PM")
    with raises(ValueError):
        convert("9 AM - 5 PM")
    with raises(ValueError):
        convert("cat")
