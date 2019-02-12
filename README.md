# getter
A shortcut for importing music from youtube into your dj library
## Requirements:
You need to have Autohotkey and Python 3 installed.  
You also need the urllib and youtube-dl library.
## Setup:
1. Set your desired output destination in destination.txt and your renderlocation in renderlocation.txt . eg  
``` C:/aFolder/ ```
2. Start getter.ahk

_On rekordbox, you should set your destination as your "automatically ad to iTunes" folder. Connecting Rekordbox to iTunes using xml-import is the easiest way to update your library on on the fly on this platform._
## Usage:
1. search for a song you want to play in a dj software of your choice
2. realise you don't have the song on you computer.
    - ohshit.jpg
3. simply press the getter hotkey (ctrl + 0 by default.)
4. getter will download the song off youtube.
    - its progress will be shown in a console window
    - this should take arount 5-10 seconds depending on your processor speed and internet connection
5. the song should appear in your software now.
    - if you're using rekordbox in conjunction with itunes, you may have to wait an additional ~10 seconds and/or press the refresh button next to the itunes tab in your track browser.
6. ???
7. Profit
