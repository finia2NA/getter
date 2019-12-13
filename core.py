from typing import Dict

import sys
import os
import shutil
import tempfile

import youtube_dl
import json


def getSettings() -> Dict[str, str]:
  with open("settings.json", 'r') as j:
    return json.load(j)


def getTempLocation() -> str:
  return tempfile.mkdtemp()


def deleteLocation(location: str) -> None:
  shutil.rmtree(location)


def getOpts(tempLocation: str): return {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "wav",
            "preferredquality": "192",
        }
    ],
    "outtmpl": tempLocation + "/%(title)s.%(ext)s",
}


def movefiles(tempLocation: str) -> None:
  source = tempLocation
  dest = getSettings()["destination"]

  files = os.listdir(source)
  for f in files:
    shutil.move(source + "/" + f, dest)


def download(url: str) -> None:
  print(url)
  tempLocation: str = getTempLocation()

  with youtube_dl.YoutubeDL(getOpts(tempLocation)) as ydl:
    ydl.download([url])

  movefiles(tempLocation)

  deleteLocation(tempLocation)


if __name__ == "__main__":
  if len(sys.argv) > 1:
    download(sys.argv[1])
