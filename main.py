import sys
import os

from lib.bootstrap import bootstrap, check_bootstrap
from lib.lib import convert_mp4_to_mp3, download

def main():
        
    # "bootstrap" command

    if (len(sys.argv) == 2) and ("bootstrap" in sys.argv or "-b" in sys.argv):
        if not check_bootstrap():
            
            bootstrap_return_code = bootstrap()

            if bootstrap_return_code != 0:
                print("error bootstrapping project (downloading binaries)")
                os._exit(1)
            else:
                print("bootstrap successeful")
                os._exit(0)
   
        else:
            print("bootstrap is already completed")
            os._exit(0)
                
    
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
