import re
from pathlib import Path
import sys
import subprocess
import os

_platform_binary_dir = "win" if sys.platform == "win32" else "unix"
_platform_binary_ext = ".exe" if sys.platform == "win32" else ""

_CONVERTED_FILES_DIR = os.getcwd() + "/converted"
_BINARY_YTDLP_PATH = os.getcwd(
) + f"/binaries/{_platform_binary_dir}/yt-dlp{_platform_binary_ext}"
_BINARY_FFMPEG_PATH = os.getcwd(
) + f"/binaries/{_platform_binary_dir}/ffmpeg{_platform_binary_ext}"
print("platform " + _BINARY_FFMPEG_PATH, _BINARY_YTDLP_PATH)


def download():
    if not os.path.exists(_CONVERTED_FILES_DIR):
        os.mkdir(_CONVERTED_FILES_DIR)

    os.chdir(_CONVERTED_FILES_DIR)

    if len(sys.argv) < 2:
        print("no url provided")
        print_usage()
        os._exit(1)
    else:
        link = sys.argv[1]

        return subprocess.call(
            [f"{_BINARY_YTDLP_PATH} -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4 {link}"], shell=True)


def convert_mp4_to_mp3(output_path_set = ""):
    
    dir_path = Path(os.getcwd())
    video_extensions = [".wedm", ".mp4", ".mkv",
                        ".flv", ".wmv", ".avi", ".mpg", ".mpeg"]

    video_files = [str(item) for item in dir_path.iterdir()
                   if item.suffix in video_extensions]

    print(video_files)

    # TODO: output file path from _get_output_filepath

    output_filename = sys.argv[2] if len(
        sys.argv) > 3 and not sys.argv[2].startswith("-") else re.escape(video_files[0])
    subprocess.call(
        [f"{_BINARY_FFMPEG_PATH} -i {re.escape(video_files[0])} {output_filename}.mp3"], shell=True)
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


def print_error(error):
    print('\033[91m' + error + '\033[0m')


def _get_output_filepath(filepath_set, initial_filepath):

    is_ui_mode = "-ui" in sys.argv

    filepath_res = initial_filepath if initial_filepath != "" else sys.argv[2] if len(
        sys.argv) > 3 and not sys.argv[2].startswith("-") else re.escape(initial_filepath)

    return filepath_res
