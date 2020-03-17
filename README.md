# 🍅 Tomato Clock
![Python package](https://github.com/coolcode/tomato-clock/workflows/Python%20package/badge.svg?branch=master)

Tomato Clock is a simple command line pomodoro app.

Pomodoro 番茄工作法 https://en.wikipedia.org/wiki/Pomodoro_Technique

## Installation

Install python3

```
$ chmod +x tomato.py
$ (optional) brew install terminal-notifier 
```
For notification, please refer to terminal-notifier -> https://github.com/julienXX/terminal-notifier#download
<img src="https://github.com/coolcode/tomato-clock/blob/master/screenshot.png?raw=true" alt="terminal-notifier" width="200"/>

## How to use
```
====== 🍅 Tomato Clock =======
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
