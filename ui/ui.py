import PySimpleGUI as ui
import lib.gtm as gtm

_UI_EVENT_CONVERT = "-CONVERT-"
_UI_KEY_FOLDER    = "-FOLDER-"
_UI_KEY_URL       = "-URL-"
_UI_KEY_LOGGER    = "-LOGGER-"


def display_gui():
    url_row =  [
        ui.Text("youtube url to download"),
        ui.In(key=_UI_KEY_URL),
    ],
    file_row =  [
               ui.Text("and save file in"),
               ui.FolderBrowse(_UI_KEY_FOLDER)
    ]
    
    actions_row = [
            ui.Button("Convert", key=_UI_EVENT_CONVERT)
    ]

    logger_row = [
        ui.Output(size=(50,20), key=_UI_KEY_LOGGER)
    ]
    
    # layout

    layout = [
        # 1 row
        url_row,
        # 2 row
        file_row,      
        # 3 row
        actions_row,
        # 4 row
       logger_row
    ]

    # window
    window = ui.Window("gtm", layout, size=(600, 800))


    # event loop

    while True:
        event, values = window.read() #pyright:ignore
        if event == ui.WINDOW_CLOSED:
            break
        elif event == _UI_EVENT_CONVERT:
            # gtm.print_error("example error")

            # TODO: test it
            download_code = gtm.download()
            
