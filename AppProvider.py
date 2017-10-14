import glob
import os
import psutil
from gi.repository import Gtk

OS_NAME = os.uname()[0]
APP_ICON_DIR = None
APP_ENTRY_DIR = None
APP_ENTRY_REGEX = None

if OS_NAME == "Linux":
    APP_ICON_DIR = [
        "/usr/share/icons/" + Gtk.Settings.get_default().get_property("gtk-icon-theme-name") + "/*/*/*/",
        "/usr/share/pixmaps/"]
    APP_ENTRY_DIR = "/usr/share/applications"
    APP_ENTRY_REGEX = "*.desktop"
    from xdg.DesktopEntry import DesktopEntry
elif OS_NAME == "Windows":
    pass
elif OS_NAME == "Mac OS":
    pass
else:
    raise Exception("Unsupported OS")

APP_PATH_REGEX = os.path.join(APP_ENTRY_DIR, APP_ENTRY_REGEX)

class AppProvider:
    @staticmethod
    def getProcess(process_name):
        for pid in psutil.pids():
            try:
                p = psutil.Process(pid)
                if p.name() == process_name:
                    return p
            except:
                pass
        return None

    @staticmethod
    def killApp(process_name):
        p = AppProvider.getProcess(process_name)
        if p:
            p.kill()

    @staticmethod
    def isAppRunning(process_name):
        p = AppProvider.getProcess(process_name)
        return p != None

    @staticmethod
    def getAppList():
        """ returns app_detail = (exec_path, icon_path)"""
        if not (APP_ICON_DIR and APP_ENTRY_DIR):
            return []
        return AppProvider.linuxAppDetails()

    @staticmethod
    def appDetails():
        """ return the appropriate app details in format: (exec_path, icon_path)"""
        if OS_NAME == "Linux":
            return AppProvider.linuxAppDetails()
        return []

    @staticmethod
    def linuxAppDetails():
        """ get linux desktop file details """
        files = []
        # probe .desktop files
        for filename in glob.glob(APP_PATH_REGEX):
            de = DesktopEntry(filename)
            exec_path = de.getExec().split(" ")[0]
            icon_path = None

            # probe all possible icon dirs
            for icon_dir in APP_ICON_DIR:
                path = icon_dir + de.getIcon() + ".*"
                regex = glob.glob(path)
                if regex:
                    icon_path = regex[0]
                    break
            # add icon path if exists
            if icon_path:
                files.append((exec_path, icon_path))
        return files
