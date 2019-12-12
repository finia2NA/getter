import sys
import youtube_dl
import os
import shutil
import tempfile as tempy


def getDestination() -> str:
  return open("destination.txt", "r").read()


def getRenderLocation() -> str:
  return open("renderlocation.txt", "r").read()


def getTempLocation() -> str:
  return tempy.mkdtemp()


def deleteLocation(location: str) -> None:
  shutil.rmtree(location)


def getOpts(): return {
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


def movefiles() -> None:
  source = getRenderLocation()
  dest = getDestination()

  files = os.listdir(source)
  for f in files:
    shutil.move(source + f, dest)


def urlToFile(url: str) -> None:
  print(url)

  with youtube_dl.YoutubeDL(getOpts()) as ydl:
    ydl.download([url])

  movefiles()


if __name__ == "__main__":
  urlToFile(sys.argv[1])
