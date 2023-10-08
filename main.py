import re
from pathlib import Path
import sys
import subprocess
import os



def download():
    converted_files_dir = os.getcwd() + "/converted"
    binary_path = os.getcwd() + "/binaries/yt-dlp"
    if not  os.path.exists(converted_files_dir):
       os.mkdir(converted_files_dir)
       
    os.chdir(converted_files_dir)

    if len(sys.argv) < 2:
        print("no url provided")
        os._exit(1)
    else:
        link = sys.argv[1]

        subprocess.call([f"{binary_path} -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4 {link}"], shell=True)


def main():
    download()
    convert_mp4_to_mp3()
        

def convert_mp4_to_mp3():
    dir_path = Path(os.getcwd())
    video_extensions = [".wedm", ".mp4", ".mkv", ".flv", ".wmv", ".avi", ".mpg", ".mpeg"]

    video_files = [str(item) for item in dir_path.iterdir() if item.suffix in video_extensions]

    print(video_files)
    output_filename = sys.argv[2] if len(sys.argv) > 3 and not sys.argv[2].startswith("-") else "output" 
    subprocess.call([f"ffmpeg -i {re.escape(video_files[0])} {output_filename}.mp3"], shell=True)
    if not "-k" in sys.argv:
        
        print(f"removing original file: {video_files[0]} -k to keep")
        os.remove(video_files[0])
    else:
        print(f"keeping original file: {video_files[0]}")
            
if __name__ == "__main__":
    main()
