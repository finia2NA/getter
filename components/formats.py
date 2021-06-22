# HOW TO ADD A FORMAT:
# - Write a function taking the render location as an input
#   and giving a dictionary of options as an output
# - Add the function to getAllFormats

from typing import Dict


def getAllFormats():
  return [wav, mp3, mp4]


def wav(tempLocation: str) -> Dict: return {
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


def mp3(tempLocation: str) -> Dict: return {
    "format": "bestaudio/best",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",
        }
    ],
    "outtmpl": tempLocation + "/%(title)s.%(ext)s",
}


def mp4(tempLocation: str) -> Dict: return {
    "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]",
    "postprocessors": [
        {
            "key": "FFmpegVideoConvertor",
            "preferedformat": "mp4",
        }
    ],
    "outtmpl": tempLocation + "/%(title)s.%(ext)s",
}
