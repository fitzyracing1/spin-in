"""A bot is plain code: it reads input, follows rules, returns an answer. No AI."""


class Bot:
    name = "bot"

    def handle(self, text: str):
        raise NotImplementedError
