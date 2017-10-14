from Config import *
from LauncherButtons import *
from AppButton import AppButton

def default_layout():
    # create default layout
    layout = Gtk.Box()
    layout.add(exit_btn())

    return layout

def app_layout(window):
    # create app layout
    layout = Gtk.Box()
    layout.add(AppButton(window))

    return layout
