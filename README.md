# spin-in

Plain bots instead of AI. Each bot is a few lines of rules and code: same input, same answer, no API, no cost, works offline.

`spin.py` asks each bot in turn and the first one that knows the answer replies.

- `rules`: keyword replies (edit `bots/rules.py`)
- `timer`: `5s`, `2 min`, `1 hour` to seconds
- `math`: exact arithmetic like `2+3*4`

Add a bot: subclass `Bot` in `bots/`, add it to `BOTS` in `spin.py`.

## Termux

```sh
pkg install -y python git gh
gh auth login
gh repo clone fitzyracing1/spin-in ~/spin-in
cd ~/spin-in && python spin.py
```

## Termux time commands (2038-safe)

A signed 32-bit seconds counter runs out on 2038-01-19 03:14:07 UTC and wraps negative. These commands do their time math in Python's unlimited-size integers through the timer bot, so they never wrap.

```sh
cd ~/spin-in && bash termux/install.sh
spin-sleep 5s          # sleeps 5 seconds on a monotonic clock
spin-secs 2 min        # 120.0
spin-date              # now, in UTC
spin-after 1 hour      # UTC time one hour from now
spin-at 2147483648     # 2038-01-19T03:14:08+00:00, one past the 32-bit limit
spin-check 2147483648  # says whether a 32-bit counter would wrap
```

They work anywhere with `python timecmd.py <command>` too. They don't change the phone's system clock or fix other apps; they give you commands that can't hit the limit.
