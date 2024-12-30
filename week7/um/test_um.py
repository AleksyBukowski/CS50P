from um import count


def test_single():
    assert count("um") == 1
    assert count(" um ") == 1


def test_comma():
    assert count("um, what is that") == 1
    assert count("Um, what is that") == 1
    assert count("um, um, um, what is that") == 3


def test_dots():
    assert count("um...") == 1


def test_questionmark():
    assert count("um?") == 1
    assert count("Um? mum? um...") == 2
    assert count("Um? mum? umm...") == 1


def test_none():
    assert count("umlaut") == 0
    assert count("yummy") == 0
    assert count("") == 0
