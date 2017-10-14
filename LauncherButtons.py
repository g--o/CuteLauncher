
from Button import *
import Launcher

# button methods
def click_exit(self, event):
    Launcher.Launcher.close_parent(self)

# buttons
def exit_btn():
    return ImageButton(IMG_APP_DEFAULT, click_exit)
