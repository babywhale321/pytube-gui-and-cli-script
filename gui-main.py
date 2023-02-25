# Importing required packages.
import requests
import re
from pytube import YouTube, Channel
import os
from easygui import *

# Establishing functions to be used in code
# This function will download a single video after user provides a link.
def download_video(link, resochoice):

    # Creating a variable to store the YouTube object for ease of use later.
    yt = YouTube(link)
    # Showing details of the selected video.
    
    if resochoice in ("l","low"):
        yt.streams.first().download()
        
    elif resochoice in ("h","high"):
        yt.streams.get_highest_resolution().download()
            

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
        with open(ytchan.channel_name + "new.txt", "w") as file:
            for url in ytchan.video_urls:
                file.write(str(url) + "\n")        
                   
        with open(ytchan.channel_name + 'old.txt', 'r') as oldlist:
            videolist1 = oldlist.read()  
        
        with open(ytchan.channel_name + 'new.txt', 'r') as newlist:
            videolist2 = newlist.read()
            
        # Saves all the new URLs into a list
        downloadlist = []
        videosplit = videolist2.split()
        for url in videosplit:
            if url not in videolist1:
                downloadlist.append(url)
                
        # Downloads all the new videos in the selected resolution.
        for url in downloadlist:
            yt = YouTube(url)
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
            # If it is a new channel, creates a file called <channelname>old.txt and writes all video urls on channel to it as a log.
        
            with open(ytchan.channel_name + "old.txt", "w") as file:
                for url in ytchan.video_urls:
                    file.write(str(url) + "\n")
            
            # Downloads all videos on channel in selected resolution.
            for video in ytchan.videos:
                if resochoice in ("l","low"):
                    video.streams.first().download()
                elif resochoice in ("h","high"):
                    video.streams.get_highest_resolution().download()                         


# This is the actual program.

while True:
    
    choices = ["Channel", "Video", "Exit"]
    msg = "Select Channel to download an entire channel\nSelect video to download a single video\n\nNOTE: the downloaded video or channel will be saved in the home directory"
    title = "Pytube GUI"
    
    # opening a choice box using our msg,title and choices
    chanloop = choicebox(msg, title, choices = choices)

    #if video is selected
    if chanloop == ("Video"):
        
        #Getting video link.
        text = "What is the YouTube URL?"
        title = "URL Selection"
        link = enterbox(text,title)
        
        #exit on cancel
        if link == None:
            break
        
        #Getting resolution choice.
        choices = ["Low","High"]
        title = "Youtube Download Quality"
        msg = "What will be the download quality?"
        reply = choicebox(msg,title, choices = choices)
        
        #low will equal l and high will equal h
        if reply == "Low":
            resochoice = "l"
            
        elif reply == "High":
            resochoice = "h"
            
        #exit on cancel
        else:
            break
        
        #try to download
        try:
            
            msg = "The download will begin.\n\nYou can watch the progress in your home directory.\nThis may take some time."
            title = "Download Confirm"
            
            #user chose continue
            if ccbox(msg, title):
                #begin download
                download_video(link, resochoice)
                msgbox("Download has completed! the saved video is in the home directory.")
                break
            
            #user chose Cancel
            else:  
                break
            
            #begin download
            download_video(link, resochoice)
            msgbox("Download has completed! the saved video is in the home directory.")
            break
        
        #ask user if they want to restart   
        except:
            
            msg = "Downloading the video has failed. Press continue to restart. Cancel to exit."
            title = "Download failed"
            
            #user chose continue
            if ccbox(msg, title):
                continue
            
            #user chose Cancel
            else:  
                break
        
    #if channel is selected
    elif chanloop == ("Channel"):
        
        #Getting channel link.
        text = "What is the youtube channels URL?"
        title = "Channel URL Selection"
        chanlink = enterbox(text,title)
        
        #exit on cancel
        if chanlink == None:
            break
            
        # Getting resolution choice.
        choices = ["Low","High"]
        title = "Youtube Download Quality"
        msg = "What will be the download quality?"
        reply = choicebox(msg,title, choices = choices)
        
        #low will equal l and high will equal h
        if reply == "Low":
            resochoice = "l"
            
        elif reply == "High":
            resochoice = "h"
            
        else:
            break
        
        try:
            
            msg = "The download will begin.\n\nYou can watch the progress in your home directory.\nThis may take some time."
            title = "Download Confirm"
            
            #user chose continue
            if ccbox(msg, title):

                #begin download
                download_video(chanlink,resochoice)
                msgbox("Download has completed! the saved channel is in the home directory.")
                break
            #user chose Cancel
            else:  
                break

        #ask user if they want to restart   
        except:
            
            msg = "Downloading the channel has failed. Press continue to restart. Cancel to exit."
            title = "Download failed"
            
            #user chose continue
            if ccbox(msg, title):
                continue
            #user chose Cancel
            else:
                break
            
    #exit input will exit    
    else:
        break
