import core

while True:
  line = input("> ")
  if line == "exit":
    break
  core.downloadUrl(core.magicSearch(line))