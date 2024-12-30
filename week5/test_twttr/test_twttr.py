from twttr import shorten

def test_word():
    assert shorten("tweet") == "twt"
    assert shorten("haha") == "hh"
    assert shorten("321") == "321"


def test_sentence():
    assert shorten("hAhA LOL") == "hh LL"
    assert shorten("Hey, thats my tweet") == "Hy, thts my twt"
    assert shorten("number 1") == "nmbr 1"


