# spin-in

[![Sponsor](https://img.shields.io/badge/Sponsor-fitzyracing1-ea4aaa?logo=githubsponsors)](https://github.com/sponsors/fitzyracing1)
[![test](https://github.com/fitzyracing1/spin-in/actions/workflows/test.yml/badge.svg)](https://github.com/fitzyracing1/spin-in/actions/workflows/test.yml)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Plain bots instead of AI. Each bot is a few lines of rules and code: same input, same answer, no API, no cost, works offline.

`spin.py` asks each bot in turn and the first one that knows the answer replies.

- `rules`: keyword replies (edit `bots/rules.py`)
- `timer`: `5s`, `2 min`, `1 hour` to seconds
- `math`: exact arithmetic like `2+3*4`

Add a bot: subclass `Bot` in `bots/`, add it to `BOTS` in `spin.py`.

## Run it

It's plain Python 3 with no packages to install, so it runs anywhere Python does.

```sh
gh repo clone fitzyracing1/spin-in
cd spin-in
python spin.py            # chat with the bots
python spin.py 5s         # one-shot answer
```

### Windows (PowerShell)
```powershell
winget install Python.Python.3.12 GitHub.cli
gh auth login
gh repo clone fitzyracing1/spin-in; cd spin-in; py spin.py
```

### Mac
```sh
brew install python gh && gh auth login
gh repo clone fitzyracing1/spin-in && cd spin-in && python3 spin.py
```

### Linux
```sh
sudo apt install -y python3 gh && gh auth login
gh repo clone fitzyracing1/spin-in && cd spin-in && python3 spin.py
```

### Termux (Android)
```sh
pkg install -y python git gh && gh auth login
gh repo clone fitzyracing1/spin-in ~/spin-in && cd ~/spin-in && python spin.py
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

## Support this project

spin-in is free and MIT licensed. If it saves you time, please [sponsor me on GitHub](https://github.com/sponsors/fitzyracing1). It keeps the bots coming.

| Plan | Price | What you get |
| --- | --- | --- |
| Free | $0 | Everything in this repo, forever |
| Pro | $49/month | Priority issues and help adding your own bots |
| Team | $199/month | Custom bots built for your team, plus Pro |

Plans are paid through [GitHub Sponsors](https://github.com/sponsors/fitzyracing1). You can also star the repo, share it, or open an issue with a bot idea.

## Author

Built by Joshua Almeida ([@fitzyracing1](https://x.com/fitzyracing1), [fitzyracing1.com](https://fitzyracing1.com), [GitHub](https://github.com/fitzyracing1)).

## License

[MIT](LICENSE) © 2026 Joshua Almeida
