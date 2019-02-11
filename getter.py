# imports
import urllib.request
import urllib.parse
import os
import sys
import re
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


def getUrl(searchString):
    query_string = urllib.parse.urlencode({"search_query": searchString})
    html_content = urllib.request.urlopen(
        "http://www.youtube.com/results?" + query_string
    )
    search_results = re.findall(
        r"href=\"\/watch\?v=(.{11})", html_content.read().decode()
    )
    return "http://www.youtube.com/watch?v=" + search_results[0]


def download(url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])


# TODO
def getAuthorAndName(url):
    return ""


# print(len(sys.argv))
# for i in range(0, len(sys.argv)):
#     print(sys.argv[i])
input = ""
for i in range(1, len(sys.argv)):
    input = input + sys.argv[i] + " "
input.strip()
print("searching for: " + input)
url = getUrl(input)
# print("found " + getAuthorAndName(url))
download(url)
