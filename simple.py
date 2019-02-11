import sys
import youtube_dl

ydl_opts = {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "outtmpl": "C:/Zwischenspeicher/%(title)s.%(ext)s",
}

url = sys.argv[1]

print(url)

with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])