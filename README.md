# Installing

1, please run windows.ps1 if you are using windows

2, please run linux.sh if you are using debian based linux

# How to use

1, after installing the required programs (' you can run windows.ps1 for windows or linux.sh for linux ')

2, download and run main.py for the cli or main-gui.py for the gui

Note: if your having issues downloading a whole channel please read this article. https://stackoverflow.com/questions/74334535/pytube-channel-video-urls-is-does-not-working

## required programs

import requests

import re

from pytube import YouTube, Channel

from pytube.cli import on_progress

import os

from easygui import *
