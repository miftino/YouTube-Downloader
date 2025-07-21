from pytube import YouTube
import sys
import os

if len(sys.argv) < 2:
    print("Usage: python script.py <YouTube URL>")
    sys.exit(1)

link = sys.argv[1]
yt = YouTube(link)

print("Title:", yt.title)
print("Views:", yt.views)

# Get the highest resolution stream
yd = yt.streams.get_highest_resolution()

# Download to Downloads folder
download_path = os.path.expanduser("~/Downloads")
yd.download(download_path)

print("Download completed to:", download_path)
