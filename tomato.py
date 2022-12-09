#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Pomodoro  https://en.wikipedia.org/wiki/Pomodoro_Technique
# ====== 🍅 Tomato Clock =======
# ./tomato.py         # start a 25 minutes tomato clock + 5 minutes break
# ./tomato.py -t      # start a 25 minutes tomato clock
# ./tomato.py -t <n>  # start a <n> minutes tomato clock
# ./tomato.py -b      # take a 5 minutes break
# ./tomato.py -b <n>  # take a <n> minutes break
# ./tomato.py -h      # help


import platform
import subprocess
import sys
import time
from itertools import count

from plyer import notification

WORK_MINUTES = 1
BREAK_MINUTES = 1


class PlatformNotSupportedException(Exception):
    """Raised when the platform is not supported by this script"""
    pass


def main():
    while True:
        try:
            # TODO: Use argsparser module
            if len(sys.argv) <= 1:
                print(f'🍅 tomato {WORK_MINUTES} minutes. Ctrl+C to exit')
                tomato(WORK_MINUTES, 'It is time to take a break')
                print(f'🛀 break {BREAK_MINUTES} minutes. Ctrl+C to exit')
                tomato(BREAK_MINUTES, 'It is time to work')

            elif sys.argv[1] == '-t':
                minutes = int(sys.argv[2]) if len(sys.argv) > 2 else WORK_MINUTES
                print(f'🍅 tomato {minutes} minutes. Ctrl+C to exit')
                tomato(minutes, 'It is time to take a break')

            elif sys.argv[1] == '-b':
                minutes = int(sys.argv[2]) if len(sys.argv) > 2 else BREAK_MINUTES
                print(f'🛀 break {minutes} minute(s). Ctrl+C to exit')
                tomato(minutes, 'It is time to work')

            elif sys.argv[1] == '-h':
                help()

            else:
                help()

        except KeyboardInterrupt:
            print('\n👋 goodbye')
            break


def tomato(minutes, notify_msg):
    start_time = time.perf_counter()
    while True:
        delta_seconds = int(round(time.perf_counter() - start_time))
        remaining_seconds = minutes * 60 - delta_seconds

        countdown = f'{int(remaining_seconds / 60)}:{int(remaining_seconds % 60):02}'

        if remaining_seconds <= 0:
            print_progress_bar(delta_seconds, minutes * 60, countdown)
            print('')
            break
        print_progress_bar(delta_seconds, minutes * 60, countdown)
        time.sleep(1)

    notify_me(notify_msg)


def print_progress_bar(current, total, countdown, prefix='\t', suffix='', length=100, fill='█', printEnd="\r"):
    """
    Call in a loop to create terminal progress bar
    """
    # print('\r', current, total, countdown, '\n')
    percent = f'{(100 * (current / float(total))):.2f}'
    filled_length = int(length * current // total)
    bar_fill = fill * filled_length + '-' * (length - filled_length)
    print(f'\r{prefix}{(countdown)}⏰ |{bar_fill}| {percent}% {suffix}', end=printEnd)
    # Print New Line on Complete
    if current == total:
        print()


def notify_me(msg):
    '''
    # macos desktop notification
    terminal-notifier -> https://github.com/julienXX/terminal-notifier#download
    terminal-notifier -message <msg>

    # ubuntu desktop notification
    notify-send

    # voice notification
    say -v <lang> <msg>
    lang options:
    - Daniel:       British English
    - Ting-Ting:    Mandarin
    - Sin-ji:       Cantonese
    '''

    print(msg)
    try:
        if sys.platform == 'darwin':
            # macos desktop notification
            subprocess.run(['terminal-notifier', '-title', '🍅', '-message', msg])
            subprocess.run(['say', '-v', 'Daniel', msg])
        elif sys.platform.startswith('linux'):
            # ubuntu desktop notification
            subprocess.Popen(["notify-send", '🍅', msg])
        elif sys.platform == 'win32':
            notification.notify(    # type: ignore
                title="Tomato Notification",
                message=msg,
                timeout=10,
                app_icon='tomato.ico'
            )
        else:
            raise PlatformNotSupportedException(
                f'The following platform is not yet supported by this script: {sys.platform}')
    except:
        # skip the notification error
        # TODO: Raise any exceptions thrown from trying to send notification
        pass


# TODO: Remove this once using argsparser module
def help():
    app_name = sys.argv[0]
    app_name = app_name if app_name.endswith('.py') else 'tomato'  # tomato is pypi package
    print('====== 🍅 Tomato Clock =======')
    print(f'{app_name}         # start a {WORK_MINUTES} minutes tomato clock + {BREAK_MINUTES} minutes break')
    print(f'{app_name} -t      # start a {WORK_MINUTES} minutes tomato clock')
    print(f'{app_name} -t <n>  # start a <n> minutes tomato clock')
    print(f'{app_name} -b      # take a {BREAK_MINUTES} minutes break')
    print(f'{app_name} -b <n>  # take a <n> minutes break')
    print(f'{app_name} -h      # help')


if __name__ == "__main__":
    main()
