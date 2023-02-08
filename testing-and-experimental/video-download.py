from pytube import YouTube
import requests
import re
import subprocess

channel_request = requests.get("https://www.youtube.com/@MentalOutlaw/videos")

pull_data = channel_request.text

regex = r"\"videoId\":\"...........\""

matches = re.findall(regex, pull_data)

matches = str(matches)

regex2 = r"[0-9a-zA-Z]{11}"

matches2 = re.search(regex2, matches)

url_end = (matches2.group())

url_front = ("https://www.youtube.com/watch?v="+url_end)

print(url_front)

user_ask = input ("Wana download it?")
if user_ask == "y":
    subprocess.run(["pytube",url_front])
else:
    print("k bye")
