from bots import time2038 as t
from timecmd import main


def test_seconds_from_timer_bot():
    assert t.seconds("5s") == 5.0
    assert t.seconds("2 min") == 120.0


def test_past_2038_does_not_wrap():
    one_past = 2**31
    assert t.would_wrap_32bit(one_past)
    assert t.to_utc(one_past).isoformat() == "2038-01-19T03:14:08+00:00"


def test_far_future():
    assert t.to_utc(2**33).year == 2242


def test_after_is_exact_past_2038():
    assert t.after("5s", start=2**31 - 1) == 2**31 + 4


def test_sleep_short():
    assert t.sleep("0 s") == 0.0


def test_cli(capsys):
    assert main(["at", "2147483648"]) == 0
    assert "2038-01-19T03:14:08" in capsys.readouterr().out
