from typing import Dict

from components import formats

import sys
import os
import shutil
import tempfile
import re

import json
import urllib.parse
import urllib.request
from validators import url as url_validate
import youtube_dl


def getSettings():
  try:
    with open("settings.json", 'r') as j:
      return json.load(j)
  except FileNotFoundError:
    FileNotFoundError("Please provide a settings.json")


def getTempLocation() -> str:
  return tempfile.mkdtemp()


def deleteLocation(location: str) -> None:
  shutil.rmtree(location)


def getOpts(tempLocation: str, format: str = "wav"):
  if format == "wav":
    return formats.wav(tempLocation)
  elif format == "mp3":
    return formats.mp3(tempLocation)
  elif format == "mp4":
    return formats.mp4(tempLocation)
  else:
    AttributeError: "Invalid format"


def movefiles(tempLocation: str, dest=getSettings()["destination"]) -> None:
  source = tempLocation
  if not os.path.exists(dest):
    os.mkdir(dest)

  files = os.listdir(source)
  for f in files:
    shutil.move(source + "/" + f, dest)


def downloadUrl(url: str, format="wav", dest=getSettings()["destination"]) -> None:
  print(url)
  tempLocation: str = getTempLocation()

  with youtube_dl.YoutubeDL(getOpts(tempLocation, format=format)) as ydl:
    ydl.download([url])

  movefiles(tempLocation, dest=dest)

  deleteLocation(tempLocation)


# imports


def search(searchString) -> str:
  query_string = urllib.parse.urlencode({"search_query": searchString})
  html_content = urllib.request.urlopen(
      "http://www.youtube.com/results?" + query_string
  )
  search_results = re.findall(
      r"href=\"\/watch\?v=(.{11})", html_content.read().decode()
  )
  return "http://www.youtube.com/watch?v=" + search_results[0]


def getArgs() -> str:
  args = ""
  for i in range(1, len(sys.argv)):
    args = args + sys.argv[i] + " "
  args.strip()
  return args


def magicSearch(toTest: str) -> None:
  if not url_validate(toTest):
    return search(toTest)
  else:
    return toTest


def main():
  searchString = getArgs()

  print("searching for: " + searchString)

  downloadUrl(magicSearch(searchString))

  print("finished")


if __name__ == "__main__" and len(sys.argv) > 1:
  main()
