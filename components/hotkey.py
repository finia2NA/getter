import keyboard
import clipboard
from components import core
import time
import random
import string

from functools import partial


def main(format=None, destination=None):
  hotkeyConfig = core.getSettings()["hotkey"]
  keyboard.add_hotkey(hotkeyConfig, partial(go, format, destination))
  keyboard.wait()


def go(format, destination):
  # get text field into clipboard
  # TODO: maybe find a way to do this keycombo-agnostic

  # unfortunatly the keyboard isn't updated immediatly when we press ctrl+x. so, we wait until we know the right value is in the clipboard
  clearstring = randomString()
  clipboard.copy(clearstring)
  keyboard.press_and_release("ctrl+a, ctrl+x")
  while clipboard.paste() == clearstring:
    pass

  # retrieve clipboard
  searchString = clipboard.paste()
  core.main(searchString, format, destination)


def randomString(stringLength=10):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

if __name__ == "__main__":
  main()
