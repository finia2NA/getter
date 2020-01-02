# getter
A multi-workflow YouTube downloader
## Requirements:
- You need to have Python 3 and PIP installed.  
- For Hotkeys, you need Autohotkey
- On Windows, you will need to have ffmpeg in your path or in the project's root directory
## Setup:
1. run `pip install -r requirements.txt` in the getter folder.
2. Copy `exampleSettings.json` into a new file named `settings.json` and set your desired settings.

## Usage
Getter supports 4 different workflows:

  - classic/AHK mode, which will download whatever is in a highlighted text field when you press the hotkey (ctrl + 0 by default)
  - core mode, which allows you to pick a path + format and then download a single video or playlist
  - interactive mode, which allows you to pick a new video or playlist to download when the first one is finished.
  - visual mode, which offers a GUI

You can use the first mode by executing getter.ahk .
You can find out information about running the other modes by running getter.py with the `-h` flag

## Planned Features
https://trello.com/b/3dv0Nx0c/getter
