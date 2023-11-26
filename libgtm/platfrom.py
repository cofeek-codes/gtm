import subprocess
import sys

def download_subprocess(binary_path, link):
    if sys.platform == "win32":
        return  subprocess.call(
            [binary_path, "-f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4", link], shell=True)
    else:
      return subprocess.call(
            [f"{binary_path} -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4, {link}"], shell=True)

def convert_subprocess(binary_path, file):
    if sys.platform == "win32":
        return subprocess.call(
        [binary_path, "-i", re.escape(file), re.escape(file) + ".mp3"], shell=True)

    else:
        return subprocess.call(
        [f"{binary_path} -i {file} {file}.mp3"], shell=True)

