import PySimpleGUI as ui


_UI_EVENT_CONVERT = "-CONVERT-"
_UI_KEY_FOLDER    = "-FOLDER-"
_UI_KEY_URL       = "-URL-"


def display_gui():

    # layout

    layout = [
        # 1 row
        [
            ui.Text("youtube url to download"),
               ui.In(key=_UI_KEY_URL),
               ],
        # 2 row
               [
               ui.Text("and save file in"),
               ui.FolderBrowse(_UI_KEY_FOLDER)
              ],
        # 3 row
        [
            ui.Button("Convert", key=_UI_EVENT_CONVERT)
        ]
              ]

    # window
    window = ui.Window("gtm", layout, size=(600, 800))

    # event loop

    while True:
        event, values = window.read() #pyright:ignore
        if event == ui.WINDOW_CLOSED:
            break
        elif event == _UI_EVENT_CONVERT:
            print(values[_UI_KEY_URL], values[_UI_KEY_FOLDER])
