from bank import value

def test_hello():
    assert value("Hello, my dear customer") == 0
    assert value("Hello") == 0
    assert value("hello there my bro") == 0


def test_h():
    assert value("hiii :3") == 20
    assert value("How are ya") == 20
    assert value("hmm...") == 20


def test_no_h():
    assert value("Wassup broski") == 100
    assert value("yo") == 100
    assert value("123") == 100
