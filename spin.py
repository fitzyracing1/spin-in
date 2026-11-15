"""spin-in: ask each bot in turn; the first one that knows the answer replies."""
import sys
from bots.timer import TimerBot
from bots.math_bot import MathBot
from bots.rules import RuleBot

BOTS = [RuleBot(), TimerBot(), MathBot()]


def spin(text):
    for bot in BOTS:
        answer = bot.handle(text)
        if answer is not None:
            return bot.name, answer
    return None, "No bot knows that yet. Add a rule in bots/rules.py."


def main():
    if len(sys.argv) > 1:
        print(*spin(" ".join(sys.argv[1:])))
        return
    print("spin-in. Type 'help', or Ctrl-D to quit.")
    for line in sys.stdin:
        print(*spin(line))


if __name__ == "__main__":
    main()
