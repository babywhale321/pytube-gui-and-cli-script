# Getting Pytube and YouTube extension
import pytube
from pytube import YouTube

# Getting link from user
link = input("Enter link of the video you would like to download:   ")
yt= YouTube(link)

# Showing video details
print("Title: ",yt.title)
print("Number of views: ",yt.views)
print("Length of video: ",yt.length)
print("Rating of video: ",yt.rating)

# Getting the highest resolution possible
ys = yt.streams.get_highest_resolution()

# Checking for confirmation of download
while True:
    usercheck = input("If you would like to download this video please type 'yes'")
    usercheck = usercheck.lower()
    if usercheck == "yes":
        
        # Starting download
        print("Downloading...")
        ys.download()
        print("Download completed!!")

    else:
        print("Did not download the video. Run program again to download a different video.")
        break
