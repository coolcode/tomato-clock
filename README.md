# 🍅 Tomato Clock
![Python package](https://github.com/coolcode/tomato-clock/workflows/Python%20package/badge.svg?branch=master)

Tomato Clock is a simple command line pomodoro app.

Pomodoro 番茄工作法 https://en.wikipedia.org/wiki/Pomodoro_Technique

## Installation

Install python from https://www.python.org/

- Install via pip:
```
$ pip install tomato-clock
$ (optional) brew install terminal-notifier 
```

- Install via source code:
```
$ git clone https://github.com/coolcode/tomato-clock.git
$ cd tomato-clock
$ chmod +x tomato.py
$ (optional) brew install terminal-notifier 
```
- terminal-notifier

For notification, please refer to terminal-notifier ➜ https://github.com/julienXX/terminal-notifier#download
<img src="https://github.com/coolcode/tomato-clock/blob/master/img/screenshot-macos.png?raw=true" alt="terminal-notifier" width="200"/>

- Ubuntu desktop notification
<img src="https://github.com/coolcode/tomato-clock/blob/master/img/screenshot-ubuntu.png?raw=true" alt="ubuntu-notification" width="200"/>


## How to use

- if you install via pip

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
🍅 tomato 25 minutes. Ctrl+C to exit
 🍅🍅---------------------------------------------- [8%] 23:4 ⏰ 
```


## Package & Publish
```
pip install setuptools wheel twine
rm -rf dist && python setup.py sdist bdist_wheel
twine upload dist/*
```

