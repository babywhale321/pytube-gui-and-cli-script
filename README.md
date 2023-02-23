# Tutorial

1, sudo apt install python3 wget -y

2, pip install pytube requests easygui

3, wget https://raw.githubusercontent.com/babywhale321/new-youtube-video-search/main/main.py

4, python3 main.py

Note: if your having issues downloading a whole channel please read this article. https://stackoverflow.com/questions/74334535/pytube-channel-video-urls-is-does-not-working

# Testing Dir

## These are required

import requests

import re

from pytube import YouTube, Channel

from pytube.cli import on_progress

import os

from easygui import *

# Objectives:
1, The goal and idea of the project is to have a python code/application that gets input from the user about what YouTube channel they would like to automatically download the newest video from that channel to a specified location.

2, If the newest video is newer than the last video that has been downloaded then the program will automatically download it.

3, If the video is the same date as the last downloaded video, then the program will exit.

4, The program will be able to run in the background and can check the specified YouTube channel “n” amount of times to see if there is a more recent video to download.

5, To have an intuitive and easy to use interface that if anything in the program fails then it can give the user a specified reason of why it failed.
      
# Success criteria:
The success of the project would be to have a working model/ prototype of the script being able to send a notice/message to the user of when a YouTube channel has uploaded a new video. A second main goal would then be to have it download the new video and store it on the PC/device the user wants it to be saved on.

# Plan Basics:
The very basic plan of our project is to have a working python program that can download videos from YouTube automatically.
