from spin import spin


def test_timer():
    assert spin("5s") == ("timer", 5.0)
    assert spin("2 min") == ("timer", 120.0)


def test_math():
    assert spin("2+3*4") == ("math", 14)


def test_rules():
    assert spin("hello") == ("rules", "Hi Joshua.")


def test_unknown():
    assert spin("what is love")[0] is None
