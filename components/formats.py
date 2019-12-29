def wav(tempLocation): return {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "192",
            }
        ],
        "outtmpl": tempLocation + "/%(title)s.%(ext)s",
    }

def mp3(tempLocation): return {
        "format": "bestaudio/best",
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }
        ],
        "outtmpl": tempLocation + "/%(title)s.%(ext)s",
    }

def mp4(tempLocation): return {
        "format": "best",
        "postprocessors": [
            {
                "key": "FFmpegVideoConvertor",
                "preferedformat": "mp4",
            }
        ],
        "outtmpl": tempLocation + "/%(title)s.%(ext)s",
    }