"""Time math that never wraps at 2038.

The 2038 problem: a signed 32-bit seconds counter tops out at 2**31-1
(2038-01-19 03:14:07 UTC) and wraps negative. Python ints have no size
limit, so every value here stays exact past 2038.
"""
import time
from datetime import datetime, timedelta, timezone

from .timer import TimerBot

INT32_MAX = 2**31 - 1
EPOCH = datetime(1970, 1, 1, tzinfo=timezone.utc)
_timer = TimerBot()


def seconds(text: str) -> float:
    """'5s' -> 5.0, '2 min' -> 120.0 via the timer bot."""
    value = _timer.handle(text)
    if value is None:
        raise ValueError(f"timer bot doesn't understand {text!r}")
    return value


def now_ns() -> int:
    """Current time as an unbounded int (nanoseconds since 1970)."""
    return time.time_ns()


def to_utc(epoch_seconds: int) -> datetime:
    """Epoch seconds to a date, built by adding to 1970 so it can't overflow a 32-bit time_t."""
    return EPOCH + timedelta(seconds=epoch_seconds)


def after(text: str, start: int | None = None) -> int:
    """Epoch seconds after a duration like '5s', from start (default now)."""
    base = now_ns() // 10**9 if start is None else start
    return base + int(seconds(text))


def would_wrap_32bit(epoch_seconds: int) -> bool:
    return epoch_seconds > INT32_MAX


def sleep(text: str) -> float:
    """Sleep using a monotonic clock, so wall-clock wraps can't cut it short."""
    total = seconds(text)
    end = time.monotonic_ns() + int(total * 1e9)
    while (left := end - time.monotonic_ns()) > 0:
        time.sleep(min(left / 1e9, 1.0))
    return total
