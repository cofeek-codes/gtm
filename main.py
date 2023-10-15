import lib.gtm as gtm
import os
import sys
from ui import ui


def main():

    gui_mode_enabled = len(sys.argv) == 2 and "-ui" in sys.argv

    if gui_mode_enabled:
        ui.display_gui()
    else:

        # cli
        return_code = gtm.download()

        if return_code != 0:
            print("error downloading file")
            os._exit(1)
        else:
            gtm.convert_mp4_to_mp3()


if __name__ == "__main__":
    main()
