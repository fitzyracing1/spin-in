# spin-in

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
