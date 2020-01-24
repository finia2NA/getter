from components import core


def main(format: str = None, dest: str = None):
  while True:
    line = input("> ")
    if line == "exit":
      break
    core.main(line, format=format, dest=dest)


if __name__ == "__main__":
  main()
