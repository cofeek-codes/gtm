import sys
import os

from libgtm.lib import convert_mp4_to_mp3, download

def main():
    
    # ui
    if "-ui" in sys.argv:
        if len(sys.argv) == 2:
            print("ui mode")
        else:
            print("if you are going to use ui version you only need to supply '-ui' flag and nothing else")
    else:
        # cli
        download_exit_code = download()
        if download_exit_code != 0:
            print("error downloading video from youtube")
            os._exit(1)
        else:
            convert_mp4_to_mp3()

if __name__ == "__main__":
    main()
