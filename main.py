# Importing required packages.
import requests
import re
from pytube import YouTube, Channel
from pytube.cli import on_progress
import os

#colors for text
class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


# Establishing functions to be used in code

# This function will download a single video after user provides a link.
def download_video(link):
    # Using a try/except to handle potential errors.
    try:
        # Creating a variable to store the YouTube object for ease of use later.
        yt = YouTube(link, on_progress_callback=on_progress)
        # Showing details of the selected video.
        print(f"Title: {yt.title}")
        print(f"Number of views: {yt.views}")
        print(f"Length of video: {yt.length}")
        print(f"Rating of video: {yt.rating}")

        usercheck = input("If you would like to download this video? (y)yes/(n)no\n")
        usercheck = usercheck.lower()
        
        if usercheck in ("yes","y"):
            # Downloads the video at highest resolution if user selected yes.
            print("Downloading...")
            yt.streams.get_highest_resolution().download()
            print("Download completed!!")

        else:
            print("Did not download the video.")
    
    except Exception as e:
        # Notifies user of any error (i.e. video is private or unlisted etc.)
        print(f"An error occurred: {e}")

# This function will download all videos from a channel or only the new videos that have not previously been downloaded.
def download_channel(chanlink, resochoice):
    # Scraping the YouTube source page for the channels true URL (non vanity url). 
    # This is a workaround for pytube not handling YouTube URLs
    channel_request = requests.get(chanlink)
    pull_data = channel_request.text
    regex = r"\"https://www.youtube.com/channel/.*?\",\""
    url_end = re.findall(regex, pull_data)
    chanurl = url_end[0].lstrip("\"").rstrip("\",\"")
    ytchan = Channel(chanurl)
    
    #will try to open the file in the (try)
    #If that fails it will assume that it is a new channel (except)
    try:

        # If not a new channel this will compare a log .txt file to a list of video URLs currently hosted on the channel.
        print("Trying to open" ,ytchan.channel_name + "new.txt\n")
        with open(ytchan.channel_name + "new.txt", "w") as file:
            for url in ytchan.video_urls:
                file.write(str(url) + "\n")        
        print(bcolors.OKGREEN + "Opening" ,ytchan.channel_name + "new.txt","was successfull\n" + bcolors.ENDC)
           
        
        print("Trying to open" ,ytchan.channel_name + "old.txt\n")        
        with open(ytchan.channel_name + 'old.txt', 'r') as oldlist:
            videolist1 = oldlist.read()
        print(bcolors.OKGREEN + "Opening" ,ytchan.channel_name + "old.txt","was successfull\n" + bcolors.ENDC)  
        
        print("Creating new updated list under", ytchan.channel_name + "new.txt\n")
        with open(ytchan.channel_name + 'new.txt', 'r') as newlist:
            videolist2 = newlist.read()
        print(bcolors.OKGREEN + "Creating" ,ytchan.channel_name + "new.txt","was successfull\n" + bcolors.ENDC) 
            
        # Saves all the new URLs into a list
        downloadlist = []
        videosplit = videolist2.split()
        for url in videosplit:
            if url not in videolist1:
                downloadlist.append(url)
        # Downloads all the new videos in the selected resolution.
        print("Downloading... this may take some time...\n")
        for url in downloadlist:
            yt = YouTube(url, on_progress_callback=on_progress)
            if resochoice in ("l","low"):
                yt.streams.first().download()
            elif resochoice in ("h","high"):
                yt.streams.get_highest_resolution().download()
        # Removes the <channelname>old.txt file and renames the new one as <channelname>old.txt to be pulled next time the program runs.
        os.remove(ytchan.channel_name + 'old.txt')
        oldname = (ytchan.channel_name + 'new.txt')
        newname = (ytchan.channel_name + 'old.txt')
        os.rename(oldname, newname)

    except:
            print(bcolors.FAIL + "Opening" ,ytchan.channel_name + "old.txt","has failed\n" +  bcolors.ENDC)   
            print("Assumeing new channel list of videos\n")
            # If it is a new channel, creates a file called <channelname>old.txt and writes all video urls on channel to it as a log.
        
            print("Creating" ,ytchan.channel_name + "old.txt\n")   
            with open(ytchan.channel_name + "old.txt", "w") as file:
                for url in ytchan.video_urls:
                    file.write(str(url) + "\n")
            print(bcolors.OKGREEN + "Creating" ,ytchan.channel_name + "old.txt","was successfull\n" +  bcolors.ENDC)  
            
            print("Downloading... this may take some time...\n")
            # Downloads all videos on channel in selected resolution.
            for video in ytchan.videos:
                if resochoice in ("l","low"):
                    video.streams.first().download()
                elif resochoice in ("h","high"):
                    video.streams.get_highest_resolution().download()                         
    print("Finished Downloading.")

# This is the actual program.


while True:
    chanloop = input("Would you like to download an entire channel or just a video? (c)channel(v)video?\n")
    chanloop = chanloop.lower()
    
    if chanloop in ("v","video"):
        # Getting video link.
        link = input("Enter link of the video you would like to download:\n")
        # Calling function
        download_video(link)
        # Exiting loop when done.
        break
    elif chanloop in ("c","channel"):
        # Getting channel link.
        chanlink = input("Enter the Channel link:\n")
        # Getting resolution choice.
        resochoice = input("Would you like to download highest quality or lowest quality? (h)high/(l)low?\n")
        resochoice = resochoice.lower()
        # Calling function.
        download_channel(chanlink,resochoice)
        # Exiting loop when done.
        break
    else:
        print("\nError: That was not a valid response. Please try again\n")
        continue
