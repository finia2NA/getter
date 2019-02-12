import sys
import youtube_dl
import os
import shutil


def getDestination():
    return open("destination.txt", "r").read()


def getRenderLocation():
    return open("renderlocation.txt", "r").read()


ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "192",
        }
    ],
    "outtmpl": getRenderLocation() + "/%(title)s.%(ext)s",
}


def movefiles():
    source = getRenderLocation()
    dest = getDestination()

    files = os.listdir(source)
    for f in files:
        shutil.move(source + f, dest)


url = sys.argv[1]

print(url)

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

movefiles()
