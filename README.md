# Youtube-Downloader-Script-
Using Python to create a simple script for downloading videos

# Simple YouTube Video Downloader
This Python script allows users to download YouTube videos in the highest available resolution using the pytube library. It's a user-friendly tool where one inputs a YouTube video URL, and the script handles the rest.

# Features
**Easy to Use**: The script prompts the user to enter the YouTube video URL they wish to download.
**Information Display**: Before downloading, it displays the video title and view count, giving the user some basic information about the video.
**High-Resolution Download**: It downloads the video in the highest available resolution.
**Age Restriction Handling**: The script checks for age restrictions and gracefully informs the user if a video cannot be downloaded due to such restrictions.

# How It Works
**YouTube Object Creation**: The script uses pytube.YouTube to create a YouTube object with the provided video link.
**Video Information**: It extracts and prints the video's title and view count for the user's reference.
**Downloading the Video**: The script selects the highest resolution available for the video and downloads it to a specified path on the user's machine.
**Error Handling**: If the video is age-restricted, the script catches the AgeRestrictedError and informs the user that the video cannot be downloaded due to these restrictions.

# Usage
Run the script and when prompted, enter the YouTube video URL you wish to download. The video will be downloaded to a path defined by you.

`python YtDownloader.py`

to run the script 

# Requirements
Python
pytube library

# Installation
Ensure Python is installed on your system. Then, install pytube using pip:

`pip install pytube`



