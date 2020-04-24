from typing import Dict

from components import formats

import sys
import os
import shutil
import tempfile
import re
from functools import reduce

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
    FileNotFoundError: "Please provide a settings.json"


def getTempLocation() -> str:
  return tempfile.mkdtemp()


def deleteLocation(location: str) -> None:
  shutil.rmtree(location)


def getOpts(tempLocation: str, format: str):
  for fun in formats.getAllFormats():
    if fun.__name__ == format:
      return fun(tempLocation)
  else:
    AttributeError: "Invalid format"


def movefiles(tempLocation: str, dest=getSettings()["destination"]) -> None:
  source = tempLocation
  if not os.path.exists(dest):
    os.mkdir(dest)

  files = os.listdir(source)
  for f in files:
    try:
      shutil.move(source + "/" + f, dest)
      print("[getter]", "moved file to", dest)
    except shutil.Error as e:
      print("[getter]", str(e), "\n...skipping")


def downloadUrl(url: str, format: str, dest: str) -> None:
  print("[getter]", "downloading:", url)
  tempLocation: str = getTempLocation()

  with youtube_dl.YoutubeDL(getOpts(tempLocation, format=format)) as ydl:
    ydl.download([url])

  movefiles(tempLocation, dest=dest)

  deleteLocation(tempLocation)

  print("[getter]", "success")


def search(searchString) -> str:
  query_string = urllib.parse.urlencode({"search_query": searchString})
  html_content = urllib.request.urlopen(
      "http://www.youtube.com/results?" + query_string
  )
  search_results = re.findall(
      r"href=\"\/watch\?v=(.{11})", html_content.read().decode()
  )
  return "http://www.youtube.com/watch?v=" + search_results[0]


def getArgs(argList: [str] = sys.argv[1:]) -> str:
  return reduce(lambda a, b: a + b + " ", argList).strip()


def magicSearch(toTest: str) -> None:
  if not url_validate(toTest):
    re = search(toTest)
    print("[getter]", "resolved", '"' + toTest+'"', "to", re)
    return re
  else:
    print("[getter]", "interpreted input as url")
    return toTest


def main(searchString: str, format: str = None, dest: str = None, shutdown: bool = False):
  if format == None:
    format = getSettings()["format"]
  if dest == None:
    dest = getSettings()["destination"]

  print("[getter]", "searching for: \"" + searchString + "\"")

  downloadUrl(magicSearch(searchString), format=format, dest=dest)

  if shutdown:
    if os.name == 'nt':
      os.system("shutdown /s /t 60")
      print("[getter]", "SHUTTING DOWN IN 1 MINUTE. PRESS ANY KEY TO ABORT")
      os.system("pause")
      os.system("shutdown /a")

    if os.name == 'posix':
      os.system("shutdown +1")
      # print("[getter]", "SHUTTING DOWN IN 1 MINUTE. PRESS ANY KEY TO ABORT")
      os.system('read -sn 1 -p "[getter] SHUTTING DOWN IN 1 MINUTE. PRESS ANY KEY TO ABORT"')
      os.system("shutdown -c")


if __name__ == "__main__" and len(sys.argv) > 1:
  main(getArgs())
