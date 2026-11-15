#!/data/data/com.termux/files/usr/bin/bash
# Installs spin-sleep, spin-secs, spin-date, spin-after, spin-at and spin-check
# into Termux's bin folder. Each one calls timecmd.py in this repo.
set -e
REPO="$(cd "$(dirname "$0")/.." && pwd)"
BIN="${PREFIX:-/data/data/com.termux/files/usr}/bin"
for c in sleep secs date after at check; do
  cat > "$BIN/spin-$c" <<SH
#!/data/data/com.termux/files/usr/bin/bash
exec python "$REPO/timecmd.py" $c "\$@"
SH
  chmod +x "$BIN/spin-$c"
done
echo "Installed: spin-sleep spin-secs spin-date spin-after spin-at spin-check"
