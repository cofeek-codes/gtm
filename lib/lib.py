import re
from pathlib import Path
import sys
import subprocess
import os
from pathlib import Path

CONVERTED_FILES_DIR = Path(os.getcwd() + "/converted")
BINARY_YTDLP_PATH   = Path(os.getcwd() + "/binaries/yt-dlp")
BINARY_FFMPEG_PATH  = Path(os.getcwd() + "/binaries/ffmpeg")


def download():
    if not os.path.exists(CONVERTED_FILES_DIR):
        os.mkdir(CONVERTED_FILES_DIR)

    os.chdir(CONVERTED_FILES_DIR)

    if len(sys.argv) < 2:
        print("no url provided")
        print_usage()
        os._exit(1)
    else:
        link = sys.argv[1]

        subprocess.call(
            [f"{BINARY_YTDLP_PATH} -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4 {link}"], shell=True)


def convert_mp4_to_mp3():
    dir_path = Path(os.getcwd())
    video_extensions = [".wedm", ".mp4", ".mkv",
                        ".flv", ".wmv", ".avi", ".mpg", ".mpeg"]

    video_files = [str(item) for item in dir_path.iterdir()
                   if item.suffix in video_extensions]

    print(video_files)
    output_filename = sys.argv[2] if len(
        sys.argv) > 3 and not sys.argv[2].startswith("-") else re.escape(video_files[0])
    subprocess.call(
        [f"{BINARY_FFMPEG_PATH} -i {re.escape(video_files[0])} {output_filename}.mp3"], shell=True)
    if not "-k" in sys.argv:

        print(f"removing original file: {video_files[0]} -k to keep")
        os.remove(video_files[0])
    else:
        print(f"keeping original file: {video_files[0]}")


def print_usage():
    print("incorrect usage")
    print(
        """


Usage:

gtm <youtube_url> (optional) <converted_filename> <flags>

converted_filename: (optional) | default "output"

flags:
	-k: keep downloaded mp4 file from deletion

        
        """
    )

