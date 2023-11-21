import shutil
import re
from pathlib import Path
import sys
import subprocess
import os

platform = "win" if sys.platform == "win32" else "unix"
extension = ".exe" if sys.platform == "win32" else ""


CONVERTED_FILES_DIR = os.path.join(os.getcwd(), "converted")
BINARY_YTDLP_PATH   = os.path.join(os.getcwd(), "binaries", platform, f"yt-dlp{extension}")
BINARY_FFMPEG_PATH  = os.path.join(os.getcwd(), "binaries", platform, f"ffmpeg{extension}")


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
        # TODO: handle errors
        download_exit_code = subprocess.call(
            [f"{BINARY_YTDLP_PATH} -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4 {link}"], shell=True)
        
        return download_exit_code

def convert_mp4_to_mp3():
    # TODO: fix renaming if have second argument
    dir_path = Path(os.getcwd())
    video_extensions = [".wedm", ".mp4", ".mkv",
                        ".flv", ".wmv", ".avi", ".mpg", ".mpeg"]

    video_files = [str(item) for item in dir_path.iterdir()
                   if item.suffix in video_extensions]

    print(video_files)

    convert_exit_code =  subprocess.call(
        [f"{BINARY_FFMPEG_PATH} -i {re.escape(video_files[0])} {re.escape(video_files[0])}.mp3"], shell=True)


    if convert_exit_code != 0:
        print("error converting video to mp3 file")
        os._exit(1)
        
    if not "-k" in sys.argv:

        print(f"removing original file: {video_files[0]} -k to keep")
        os.remove(video_files[0])
    else:
        print(f"keeping original file: {video_files[0]}")

    if len(sys.argv) >= 3 and not sys.argv[2].startswith('-'):
        
        postconvert(original_file=video_files[0] + ".mp3") # needed after convertion




def postconvert(original_file):
    print("postconvert")
    print(original_file)
    print(sys.argv[2])
    shutil.move(original_file, sys.argv[2])
    


def movefile(src,dst):

    src_file = open(src, 'r')
    dst_file = open(dst, 'w')
    
    content = src_file.read()
    dst_file.write(content)
    
    
    src_file.close()
    dst.close()

    os.remove(src)
    
def print_usage():
    print("incorrect usage")
    print(
        """


Usage:

gtm <youtube_url> (optional) <converted_filename> <flags>

converted_filename: (optional) | default is the name of downloaded video

flags:
	-k: keep downloaded mp4 file from deletion
        -ui: enable gui mode
        
        """
    )

