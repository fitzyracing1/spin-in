"""spin-in time commands (2038-safe).

  python timecmd.py sleep 5s          sleep 5 seconds
  python timecmd.py secs 2 min        print seconds (120.0)
  python timecmd.py date              current UTC time from an unbounded clock
  python timecmd.py after 5s          UTC time 5 seconds from now
  python timecmd.py at 2147483648     epoch seconds to UTC (one past the 2038 limit)
  python timecmd.py check 2147483648  does it overflow a 32-bit counter?
"""
import sys
from bots import time2038 as t


def main(argv):
    if not argv or argv[0] in ("-h", "--help", "help"):
        print(__doc__.strip())
        return 0
    cmd, arg = argv[0], " ".join(argv[1:])
    if cmd == "sleep":
        t.sleep(arg)
    elif cmd == "secs":
        print(t.seconds(arg))
    elif cmd == "date":
        print(t.to_utc(t.now_ns() // 10**9).isoformat())
    elif cmd == "after":
        print(t.to_utc(t.after(arg)).isoformat())
    elif cmd == "at":
        print(t.to_utc(int(arg)).isoformat())
    elif cmd == "check":
        n = int(arg)
        print(f"{n}: {'wraps' if t.would_wrap_32bit(n) else 'fits'} in a 32-bit counter; safe here: {t.to_utc(n).isoformat()}")
    else:
        print(f"unknown command {cmd!r}; try: python timecmd.py help", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
