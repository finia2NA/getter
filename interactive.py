import getter

while True:
  line = input("> ")
  if line == "exit":
    break
  getter.downloadUrl(getter.magicSearch(line))