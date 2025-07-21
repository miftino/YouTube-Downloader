import sys
from yt_dlp import YoutubeDL

def main():
    if len(sys.argv) < 2:
        print("Usage: python yt_downloader.py <YouTube URL>")
        sys.exit(1)

    url = sys.argv[1]

    ydl_opts = {
        'outtmpl': '%(title)s.%(ext)s',  # Save in current folder, use video title as filename
        'format': 'best',                 # Download best quality video + audio
    }

    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            print("Download complete!")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
