import lib.gtm as gtm
import os


def do_cli():

    return_code = gtm.download()

    if return_code != 0:
        print("error downloading file")
        os._exit(1)
    else:
        gtm.convert_mp4_to_mp3()
