# imports
import urllib.request
import urllib.parse
import shutil
import os
import sys
import re
from validators import url as url_validate
import youtube_dl
import core


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
  input = ""
  for i in range(1, len(sys.argv)):
    input = input + sys.argv[i] + " "
  input.strip()


def magicSearch(toTest: str) -> None:
  if url_validate(input):
    return search(input)
  else:
    return toTest


def main():
  print("searching for: " + input)
  # print("found " + getAuthorAndName(url))

  core.download(search(input))

  print("finished")


if __name__ == "__main__" and len(sys.argv) > 1:
  main()
