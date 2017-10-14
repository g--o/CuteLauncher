
from LauncherWindow import *

# app_detail is (label, icon, path)
app_detail_exit = ("Exit", None, "exit")

class AppWindow(LauncherWindow):
    def __init__(self, app):
        self.app = app
        self.layout = app_layout(self)
        super(AppWindow, self).__init__(layout = self.layout)
        self.set_keep_above(True)

    def close(self):
        self.app.close()
