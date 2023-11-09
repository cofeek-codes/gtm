import sys



from lib.lib import convert_mp4_to_mp3, download

def main():

    # ui
    if "-ui" in sys.argv:
        if len(sys.argv) == 2:
            print("ui mode")
        else:
            print("if you are going to use ui version you only need to supply '-ui' flag and nothing else")
    else:
        # cli
        download()
        convert_mp4_to_mp3()

if __name__ == "__main__":
    main()
