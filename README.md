# 🍅 Tomato Clock (Python)

[![Publish to PyPI](https://github.com/coolcode/tomato-clock/actions/workflows/package.yml/badge.svg)](https://github.com/coolcode/tomato-clock/actions/workflows/package.yml)
[![PyPI tomato-clock](https://badge.fury.io/py/tomato-clock.svg)](https://pypi.python.org/pypi/tomato-clock/)

Tomato Clock is a straightforward command-line Pomodoro application.

- [Pomodoro Technique](https://en.wikipedia.org/wiki/Pomodoro_Technique)
- [番茄工作法](https://zh.wikipedia.org/zh-cn/%E7%95%AA%E8%8C%84%E5%B7%A5%E4%BD%9C%E6%B3%95)
- [Tomato Clock (Rust)](https://github.com/coolcode/tomato-clock-rs)

## Installation

[Install python](https://www.python.org)

- Install via pip:

```sh
pip install tomato-clock
```

- Install via source code:

```sh
git clone https://github.com/coolcode/tomato-clock.git
cd tomato-clock
chmod +x tomato.py 
```

## How to use

- if you install via pip

```sh
tomato         # start a 25 minutes tomato clock + 5 minutes break
tomato -t      # start a 25 minutes tomato clock
tomato -t <n>  # start a <n> minutes tomato clock
tomato -b      # take a 5 minutes break
tomato -b <n>  # take a <n> minutes break
tomato -h      # help
```

- if you install via source code

```sh
./tomato.py         # start a 25 minutes tomato clock + 5 minutes break
./tomato.py -t      # start a 25 minutes tomato clock
./tomato.py -t <n>  # start a <n> minutes tomato clock
./tomato.py -b      # take a 5 minutes break
./tomato.py -b <n>  # take a <n> minutes break
./tomato.py -h      # help
```

## Terminal Output

```sh
🍅 tomato 25 minutes. Ctrl+C to exit
 🍅🍅---------------------------------------------- [8%] 23:04 ⏰ 
```

## Desktop Notification

- MacOS

```sh
brew install terminal-notifier 
```

`terminal-notifier` actually is a cross-platform desktop notifier, please refer to ➜ [terminal-notifier](https://github.com/julienXX/terminal-notifier#download)

<img src="https://github.com/coolcode/tomato-clock/blob/master/img/screenshot-macos.png?raw=true" alt="terminal-notifier" width="300"/>

- Ubuntu

`notify-send`

<img src="https://github.com/coolcode/tomato-clock/blob/master/img/screenshot-ubuntu.png?raw=true" alt="ubuntu-notification" width="300"/>


## Voice Notifications

Tomato Clock uses `say`(text-to-speech) for voice notifications.

- MacOS

MacOS already has `say`. see [here](https://ss64.com/osx/say.html) or [more detail](https://gist.github.com/mculp/4b95752e25c456d425c6)  

- Ubuntu

See this link: [say](http://manpages.ubuntu.com/manpages/trusty/man1/say.1.html)

```sh
sudo apt-get install gnustep-gui-runtime
```

- Windows

Check this one: https://github.com/SeanBracksDev/tomato-clock
