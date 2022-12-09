# 🍅 Tomato Clock

## Overview

Tomato Clock is a simple command line pomodoro app.

Forked from https://github.com/coolcode/tomato-clock, with my own modifications/improvements including:

- Windows Notifications.
- New and improved progress bar.
- Now continuously iterates between "work" & "rest" modes, instead of just once for each.

Pomodoro Technique: https://en.wikipedia.org/wiki/Pomodoro_Technique

## Installation

Install python from https://www.python.org/

- Install via pip:

```
$ pip install tomato-clock
```

- Install via source code:

```
$ git clone https://github.com/SeanBracksDev/tomato-clock.git
$ cd tomato-clock
$ chmod +x tomato.py
```

## How to use

- if you install via pip

> TODO: Update once arguments implemented with argsparser

```

$ tomato         # start a 25 minutes tomato clock + 5 minutes break
$ tomato -t      # start a 25 minutes tomato clock
$ tomato -t <n>  # start a <n> minutes tomato clock
$ tomato -b      # take a 5 minutes break
$ tomato -b <n>  # take a <n> minutes break
$ tomato -h      # help
```

- if you install via source code

```
$ ./tomato.py         # start a 25 minutes tomato clock + 5 minutes break
$ ./tomato.py -t      # start a 25 minutes tomato clock
$ ./tomato.py -t <n>  # start a <n> minutes tomato clock
$ ./tomato.py -b      # take a 5 minutes break
$ ./tomato.py -b <n>  # take a <n> minutes break
$ ./tomato.py -h      # help
```

## Terminal Output

```
 tomato 1 minutes. Ctrl+C to exit
        0:50⏰ |██████████--------------------------------------------------| 16.67%
```

## Desktop Notification

- MacOS

```
$ brew install terminal-notifier
```

`terminal-notifier` is a cross-platform desktop notifier, please refer to ➜ [terminal-notifier](https://github.com/julienXX/terminal-notifier#download)

<img src="https://github.com/coolcode/tomato-clock/blob/master/img/screenshot-macos.png?raw=true" alt="terminal-notifier" width="300"/>

- Ubuntu

`notify-send`

<img src="https://github.com/coolcode/tomato-clock/blob/master/img/screenshot-ubuntu.png?raw=true" alt="ubuntu-notification" width="300"/>

## Voice Notification

We use `say` (text-to-speech) for voice notification

- MacOS

MacOS already has `say`. see [here](https://ss64.com/osx/say.html) or [more detail](https://gist.github.com/mculp/4b95752e25c456d425c6)

- Ubuntu

see this link: [say](http://manpages.ubuntu.com/manpages/trusty/man1/say.1.html)

```
sudo apt-get install gnustep-gui-runtime
```
