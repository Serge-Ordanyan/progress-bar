# Terminal Progress Bar

A tiny Python app that turns your todo list into a progress bar you can fill in from the terminal.

## Why I made this

I keep my todo list on paper. It's split into subtitles, and under each subtitle I write its tasks. Crossing things off on paper feels great, but I could never see the whole picture at a glance: how much of the list is actually done?

I didn't want a heavy todo app with accounts and sync. I wanted something simple: one piece of a bar per subtitle, and when a subtitle is finished, that piece turns green. So I built this small app to do exactly that, right in the terminal.

## Features

- Set the number of subtitles as a parameter, and the bar splits into that many pieces
- Finished pieces turn green
- Live percentage shown above the bar
- Toggle any piece on and off (draw it or rub it out)
- No dependencies, only the Python standard library

## Usage

```bash
python3 progress.py 6
```

`6` is the number of subtitles. If you leave it off, the app asks for it.

## Controls

| Key | Action |
| --- | --- |
| `←` / `→` | Move between pieces |
| `Space` / `Enter` | Toggle the selected piece |
| `1`-`9` | Toggle that piece directly |
| `r` | Reset everything |
| `q` | Quit |

## Requirements

- Python 3
- A terminal (tested on macOS)

The bar needs about 7 characters per piece, so with many subtitles use a wider terminal window.
