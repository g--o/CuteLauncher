from App import App
from AppWindow import *
from AppProvider import AppProvider

REFRESH_RATE = 1 # seconds

class Launcher(object):

    def __init__(self):
        # Create Apps
        self.apps = {}
        self.num_windows = 0
        self.last_slot = self.num_windows
        self.createApps()

    def createApps(self):
        # create app launchers
        self.apps = {}

        for app_detail in AppProvider.getAppList(True):
            self.apps[app_detail[0]] = App(self, app_detail)
            self.apps[app_detail[0]].window.hide()

    def update(self):
        AppProvider.update()
        print "[CuteLauncher] GUI update"
        for app in self.apps.values():
            if not app.set_running(AppProvider.isAppRunning(app.exec_path)):
                continue
            self.last_slot = max(self.last_slot + 1, self.num_windows)
            app_width, app_height = Clickable.SIZE
            screen_width, screen_height = app.window.get_screen_size()
            app.move(self.last_slot * app_width, screen_height - app_height)
        return True

    def start(self):
        print "[CuteLauncher] Starting..."
        GLib.threads_init()
        GLib.timeout_add_seconds(REFRESH_RATE, self.update)
        Gtk.main()

    def show_app(self, app):
        self.num_windows += 1

    def hide_app(self, app):
        self.num_windows -= 1

    def focus_app(self, app):
        AppProvider.focusApp(app.exec_path)

    def close_app(self, app):
        AppProvider.killApp(app.exec_path)

    @staticmethod
    def close_parent(btn):
        btn.get_parent_window().destroy()
        Launcher.num_windows -= 1

        if (Launcher.num_windows <= 0):
            Gtk.main_quit()
