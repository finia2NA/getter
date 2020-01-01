import core
def main():
  while True:
    line = input("> ")
    if line == "exit":
      break
    core.downloadUrl(core.magicSearch(line))

if __name__ == "__main__":
    main()