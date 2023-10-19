import shutil
import re
from pathlib import Path
import sys
import subprocess
import os

is_gui_mode = len(sys.argv) == 2 and "-ui" in sys.argv

_platform_binary_dir = "win" if sys.platform == "win32" else "unix"
_platform_binary_ext = ".exe" if sys.platform == "win32" else ""

_CONVERTED_FILES_DIR = os.getcwd() + "/converted"
_BINARY_YTDLP_PATH = os.getcwd(
) + f"/binaries/{_platform_binary_dir}/yt-dlp{_platform_binary_ext}"
_BINARY_FFMPEG_PATH = os.getcwd(
) + f"/binaries/{_platform_binary_dir}/ffmpeg{_platform_binary_ext}"
print("platform " + _BINARY_FFMPEG_PATH, _BINARY_YTDLP_PATH)

# TODO: probuably rename arg
def download(gui_link = None):


    if not is_gui_mode:
        
        if not os.path.exists(_CONVERTED_FILES_DIR):
            os.mkdir(_CONVERTED_FILES_DIR)

        os.chdir(_CONVERTED_FILES_DIR)

        if len(sys.argv) < 2:
            print("no url provided")
            print_usage()
            os._exit(1)
        else:
            link = sys.argv[1]

            return subprocess.Popen(
                f"{_BINARY_YTDLP_PATH} -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4 {link}".split(' '), stdin=subprocess.PIPE)
    else:
        return subprocess.Popen(
                f"{_BINARY_YTDLP_PATH} -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4 {gui_link}".split(' '), stdin=subprocess.PIPE)

        
def convert_mp4_to_mp3(gui_path = None):
    
    dir_path = Path(os.getcwd())
    video_extensions = [".wedm", ".mp4", ".mkv",
                        ".flv", ".wmv", ".avi", ".mpg", ".mpeg"]

    video_files = [str(item) for item in dir_path.iterdir()
                   if item.suffix in video_extensions]

    print(video_files)

    # TODO: output file path from _get_output_filepath
    print("video_files")
    print(video_files)

    output_filename = _get_output_filepath(video_files[0])                                       
    ffmpeg_process_returncode = subprocess.Popen(
        f"{_BINARY_FFMPEG_PATH} -i {re.escape(video_files[0])} {output_filename}.mp3".split(' '), stdin=subprocess.PIPE)

    _AUDIO_EXTENSION = ".mp3"
    audio_files = [str(item) for item in dir_path.iterdir()
                   if item.suffix == _AUDIO_EXTENSION]
    print("audio_files")
    print(audio_files)
    
    converted_file = audio_files[0]
    print(converted_file)
    if gui_path != None:
        shutil.move(converted_file, gui_path)
    if not "-k" in sys.argv:

        print(f"removing original file: {video_files[0]} -k to keep")
        os.remove(video_files[0])
    else:
        print(f"keeping original file: {video_files[0]}")

    return ffmpeg_process_returncode

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
