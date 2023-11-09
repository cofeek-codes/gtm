import sys

from lib.lib import convert_mp4_to_mp3, download

def main():
    # ui
    if "-ui" in sys.argv:
        print("ui mode")
    else:
        # cli
        download()
        convert_mp4_to_mp3()

if __name__ == "__main__":
    main()
