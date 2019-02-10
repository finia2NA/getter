# imports
import urllib.request
import urllib.parse
import os
import sys
import re


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
    os.system(
        "youtube-dl.exe "
        + url
        + "-x, --extract-audio "
        + "--audio-format mp3 "
        + "--audio-quality 0 "
        + "-f bestaudio"
        # + "--no-playlist"
        # + "-o 'C:\\Users\\User\\Downloads\\%(title)s.%(ext)s'"
    )


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
