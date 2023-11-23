from pytube import YouTube
from pytube.exceptions import AgeRestrictedError

link = input("Enter the YouTube video URL you wish to download: ")

try :
    yt = YouTube(link)           # Create a YouTube object with the provided link


    print("Title: ", yt.title)   # Print the title of the YouTube video
    print("Views: ", yt.views)   # Print the number of views of the YouTube video

    # Get the highest resolution stream available for the video
    yd = yt.streams.get_highest_resolution()


    # Download the video to the specified path. The 'r' before the string
    # makes it a raw string, so backslashes are treated literally and not
    # as escape characters
    yd.download(r"C:\Users\hell_pc\Videos\Youtube Vidoes")

except AgeRestrictedError:
    print(f"The video {link} is age restricted and cannot be downloaded.")



# NOTES

# Found Out that the Pytube can't download videos that are age restricted as it cannot perform the necessary authentication. 

# ( In the pytube library, the get_highest_resolution() function selects the highest resolution stream that contains both video 
#   and audio in a single file. Typically, these streams are available up to 720p. For higher resolutions, like 1080p, 1440p (2K), or 2160p (4K), 
#   the video and audio are usually separated into different streams by YouTube. This means you would need to download both streams separately and then combine them.)
