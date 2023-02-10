# Importing required packages.
import requests
import re
from pytube import YouTube, Channel
from pytube.cli import on_progress
import os
from easygui import *

#colors for text
class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

# Establishing functions to be used in code
# This function will download a single video after user provides a link.
def download_video(link, resochoice):
    # Using a try/except to handle potential errors.
    try:
        # Creating a variable to store the YouTube object for ease of use later.
        yt = YouTube(link, on_progress_callback=on_progress)
        # Showing details of the selected video.
        print(f"Title: {yt.title}")
        print(f"Number of views: {yt.views}")
        print(f"Length of video: {yt.length}")
        print(f"Rating of video: {yt.rating}")

        print("Downloading...\n")
        
        if resochoice in ("l","low"):
            yt.streams.first().download()
            print("\n")
            
        elif resochoice in ("h","high"):
            yt.streams.get_highest_resolution().download()
            print("\n")
            
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
        print(bcolors.OKGREEN + "Opening" ,ytchan.channel_name + "new.txt","was successful\n" + bcolors.ENDC)
           
        print("Trying to open" ,ytchan.channel_name + "old.txt\n")        
        with open(ytchan.channel_name + 'old.txt', 'r') as oldlist:
            videolist1 = oldlist.read()
        print(bcolors.OKGREEN + "Opening" ,ytchan.channel_name + "old.txt","was successful\n" + bcolors.ENDC)  
        
        print("Creating new updated list under", ytchan.channel_name + "new.txt\n")
        with open(ytchan.channel_name + 'new.txt', 'r') as newlist:
            videolist2 = newlist.read()
        print(bcolors.OKGREEN + "Creating" ,ytchan.channel_name + "new.txt","was successful\n" + bcolors.ENDC) 
            
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
            print(bcolors.OKGREEN + "Creating" ,ytchan.channel_name + "old.txt","was successful\n" +  bcolors.ENDC)  
            
            print("Downloading... this may take some time...\n")
            # Downloads all videos on channel in selected resolution.
            for video in ytchan.videos:
                if resochoice in ("l","low"):
                    video.streams.first().download()
                elif resochoice in ("h","high"):
                    video.streams.get_highest_resolution().download()                         
    print("Finished Downloading.")

# This is the actual program.
choices = ["Channel", "Video", "Exit"]
msg = "Select Channel to download an entire channel\nSelect video to download a single video."
title = "python pytube gui"
# opening a choice box using our msg,title and choices
chanloop = choicebox(msg, title, choices = choices)

#if video is selected
if chanloop == ("Video"):
    
    #Getting video link.
    text = "What is the YouTube url?"
    title = "url selection"
    link = enterbox(text,title)
    
    #exit on cancel
    if link == None:
        exit()
    
        # Getting resolution choice.
    choices = ["Low","High"]
    title = "Youtube Download Quality"
    msg = "Download Quality?"
    reply = choicebox(msg,title, choices = choices)
    
    #low will equal l and high will equal h
    if reply == "Low":
        resochoice = "l"
        
    elif reply == "High":
        resochoice = "h"
        
    else:
        exit()
        
    #Calling function
    download_video(link, resochoice)
    
#if channel is selected
elif chanloop == ("Channel"):
    
    #Getting channel link.
    text = "What is the Channels url?"
    title = "channel url selection"
    chanlink = enterbox(text,title)
    
    #exit on cancel
    if chanlink == None:
        exit()
        
    # Getting resolution choice.
    choices = ["Low","High"]
    title = "Youtube Download Quality"
    msg = "Download Quality?"
    reply = choicebox(msg,title, choices = choices)
    
    #low will equal l and high will equal h
    if reply == "Low":
        resochoice = "l"
        
    elif reply == "High":
        resochoice = "h"
        
    else:
        exit()
        
    # Calling function.
    download_channel(chanlink,resochoice)
    
else:
    exit()
