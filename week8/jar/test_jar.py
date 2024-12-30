from jar import Jar
import pytest

def test_init():
    jar1 = Jar(5)
    assert jar1.capacity == 5
    jar2 = Jar(2)
    assert jar2.capacity == 2
    jar3 = Jar()
    assert jar3.capacity == 12
    with pytest.raises(ValueError):
        jar4 = Jar(-5)
    with pytest.raises(ValueError):
        jar4 = Jar("abc")




def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert jar.size == 1
    jar.deposit(7)
    assert jar.size == 8
    with pytest.raises(ValueError):
        jar.deposit(120)


def test_withdraw():
    jar = Jar(20)
    jar.deposit(18)
    assert jar.size == 18
    jar.withdraw(5)
    assert jar.size == 13

    with pytest.raises(ValueError):
        jar.withdraw(-10)

    jar.withdraw(13)
    assert jar.size == 0

    with pytest.raises(ValueError):
        jar.withdraw(5)
