import re
from .base import Bot

UNITS = {"s": 1, "sec": 1, "second": 1, "seconds": 1, "m": 60, "min": 60, "minute": 60,
         "minutes": 60, "h": 3600, "hour": 3600, "hours": 3600}


class TimerBot(Bot):
    """Turns '5s', '2 min', '1 hour' into seconds."""
    name = "timer"

    def handle(self, text):
        m = re.fullmatch(r"\s*(\d+(?:\.\d+)?)\s*([a-z]+)\s*", text.lower())
        if not m or m.group(2) not in UNITS:
            return None
        return float(m.group(1)) * UNITS[m.group(2)]
