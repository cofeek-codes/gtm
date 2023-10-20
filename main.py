import sys
from ui import ui
from cli import cli


def main():

    is_gui_mode = len(sys.argv) == 2 and "-ui" in sys.argv

    # ui
    if is_gui_mode:

        ui.display_gui()

    else:

        # cli
        cli.do_cli()


if __name__ == "__main__":
    main()
