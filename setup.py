#!/usr/bin/env python

from distutils.core import setup

description = "Tomato Clock is a simple command line pomodoro app"
long_description = """
Tomato Clock is a simple command line pomodoro app.
The Pomodoro technique is a time management technique for improving productivity.
Check (https://en.wikipedia.org/wiki/Pomodoro_Technique) for more details.
Github (https://github.com/coolcode/tomato-clock)
"""


setup(
    name="tomato-clock",
    version="0.0.2",
    author="Bruce Lee",
    author_email="bruce.meerkat@gmail.com",
    description=description,
    long_description=long_description,
    license="MIT",
    keywords="pomodoro,tomato,tomato-timer,terminal,terminal-app,pomodoro-timer",
    url="https://github.com/coolcode/tomato-clock",
    classifiers=['Intended Audience :: Science/Research',
                 'Intended Audience :: Developers',
                 'License :: OSI Approved :: MIT License',
                 'Programming Language :: Python',
                 'Topic :: Software Development',
                 'Topic :: Scientific/Engineering',
                 'Operating System :: Microsoft :: Windows',
                 'Operating System :: POSIX',
                 'Operating System :: Unix',
                 'Operating System :: MacOS'],
    platforms='any',
    scripts=['tomato.py'],
    include_package_data=True
)