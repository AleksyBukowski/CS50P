from seasons import minutes_since
from datetime import date

today = date.today()

def test_dates():
    assert minutes_since(str(today)) == 0
    assert minutes_since("2004-02-13") == int((today - date.fromisoformat("2004-02-13")).total_seconds() / 60)
