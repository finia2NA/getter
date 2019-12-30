import getter

line: str = ""
while line!="exit":
  line = input()
  getter.downloadUrl(getter.magicSearch(line))