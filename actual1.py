# imports
import urllib.request
import urllib.parse
import re
import os

# mp3 parameters
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def getUrl(searchString):
  query_string = urllib.parse.urlencode({"search_query" : searchString})
  html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
  search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
  return ("http://www.youtube.com/watch?v=" + search_results[0])

def download(url):
  os.system("youtube-dl.exe " + url + "-x, --extract-audio --audio-format mp3 -o "/output")