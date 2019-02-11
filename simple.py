import sys
import youtube_dl

def getLocation():
    return open ("destination.txt", "r").read()

ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "outtmpl": getLocation() + "/%(title)s.%(ext)s",
}


url = sys.argv[1]

print(url)

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])