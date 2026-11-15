from .base import Bot


class RuleBot(Bot):
    """Keyword -> reply table. Edit RULES to teach it."""
    name = "rules"
    RULES = {
        "hello": "Hi Joshua.",
        "status": "All bots up.",
        "help": "Try: 5s, 2 min, 2+3*4, hello, status, sponsor",
        "sponsor": "Thanks! https://github.com/sponsors/fitzyracing1",
    }

    def handle(self, text):
        return self.RULES.get(text.strip().lower())
