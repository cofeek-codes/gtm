import shutil
import re
from pathlib import Path
import sys
import subprocess
import os

is_gui_mode = len(sys.argv) == 2 and "-ui" in sys.argv

_platform_binary_dir = "win" if sys.platform == "win32" else "unix"
_platform_binary_ext = ".exe" if sys.platform == "win32" else ""


# TODO: fix paths

_CONVERTED_FILES_DIR = os.getcwd() + "/converted"
_BINARY_YTDLP_PATH = os.getcwd(
) + f"/binaries/{_platform_binary_dir}/yt-dlp{_platform_binary_ext}"
_BINARY_FFMPEG_PATH = os.getcwd(
) + f"/binaries/{_platform_binary_dir}/ffmpeg{_platform_binary_ext}"
print("platform " + _BINARY_FFMPEG_PATH, _BINARY_YTDLP_PATH)

# TODO: probuably rename arg


def download(gui_link=None):

    if not os.path.exists(_CONVERTED_FILES_DIR):
        os.mkdir(_CONVERTED_FILES_DIR)

    os.chdir(_CONVERTED_FILES_DIR)

    if not is_gui_mode:

        if len(sys.argv) < 2:
            print("no url provided")
            print_usage()
            os._exit(1)
        else:
            link = sys.argv[1]

            return subprocess.Popen(
                f"{_BINARY_YTDLP_PATH} -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4 {link}", stdin=subprocess.PIPE)
    # gui mode
    else:
        print("gui link")
        print(gui_link)

        if gui_link == None:
            print("no url provided")
            print_usage()
            os._exit(1)
        else:

            return subprocess.Popen(
                f"{_BINARY_YTDLP_PATH} -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4 {gui_link}".split(' '), stdin=subprocess.PIPE)


def convert_mp4_to_mp3(gui_path=None):

    dir_path = Path(_CONVERTED_FILES_DIR)
    video_extensions = [".wedm", ".mp4", ".mkv",
                        ".flv", ".wmv", ".avi", ".mpg", ".mpeg"]

    video_files = [str(item) for item in dir_path.iterdir()
                   if item.suffix in video_extensions]

    print(os.getcwd())
    print(video_files)

    _postconvert()


def _postconvert():
    print("postconvert executed")


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


def print_error(error):
    print('\033[91m' + error + '\033[0m')


def _get_output_filepath(initial_filepath):
    output_filename = sys.argv[2] if len(
        sys.argv) > 3 and not sys.argv[2].startswith("-") else initial_filepath

    return output_filename
