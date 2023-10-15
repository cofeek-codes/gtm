import PySimpleGUI as ui


def display_gui():

    # layout

    layout = [[ui.Text("youtube url to download")]]

    # window
    window = ui.Window("gtm", layout, margins=(200, 300))

    # event loop

    while True:
        event, values = window.read()
