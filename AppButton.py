import Launcher
from Button import ImageButton

class AppButton(ImageButton):
    def __init__(self, app_window):
        """ create app object from (exec_path, icon_path) """
        self.app_window = app_window
        super(AppButton, self).__init__(app_window.app.icon_path, self.app_click)

    def app_click(self, widget, event):
        self.app_window.close()
