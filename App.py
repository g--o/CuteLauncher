from Config import *
from AppWindow import AppWindow

class App(object):
    def __init__(self, launcher, app_details):
        self.launcher = launcher
        self.exec_path, self.icon_path = app_details
        self.window = AppWindow(self)
        self.is_running = False

    def move(self, x, y):
        self.window.move(x, y)

    def show(self):
        self.launcher.show_app(self)
        self.window.show()
        self.window.set_keep_above(True)

    def hide(self):
        self.launcher.hide_app(self)
        self.window.hide()

    def close(self):
        self.launcher.close_app(self)

    def focus(self):
        self.launcher.focus_app(self)

    def set_running(self, is_running):
        if self.is_running == is_running:
            return False
        if is_running:
            self.show()
        else:
            self.hide()
        self.is_running = is_running
        return True
