import requests
import re

while True:
    chanloop = input ("Would you like to download an entire channel or just a video?  c/v")
    if chanloop == "c":
        chanlink = input("Enter the Channel link:   ")

        channel_request = requests.get(chanlink)
        pull_data = channel_request.text
        regex = r"\"https://www.youtube.com/channel/.*?\",\""
        matches = re.search(regex, pull_data)
        url_end = (matches.group())
        url_end = str(url_end)
        chanurl = (url_end.lstrip("\"").rstrip("\",\""))

        ytchan = Channel(chanurl)
        print (f"Downloading videos from: {ytchan.channel_name} ")
    else:
        break
