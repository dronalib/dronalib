import dronalib


def test_say_hello():
    dronalib.say_hello()


def test_fail_on_purpose():
    raise ValueError
