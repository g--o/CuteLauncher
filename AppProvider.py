import glob
import psutil
from Config import *
from ProcessNotifier import ProcessNotifier
from gi.repository import GdkX11

UPDATE_APP_ENTRIES = False
APP_BLACK_LIST = []

if OS_NAME == "Linux":
    APP_BLACK_LIST = [ "nautilus", "compiz" ]

class AppProvider:
    apps = []

    @staticmethod
    def update():
        AppProvider.getAppList(UPDATE_APP_ENTRIES)
        ProcessNotifier.update()

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
    def focusApp(process_name):
        now = GdkX11.x11_get_server_time(Gdk.get_default_root_window())
        return ProcessNotifier.getOpenProcsCached()[process_name].activate(now)

    @staticmethod
    def killApp(process_name):
        p = AppProvider.getProcess(process_name)
        if p:
            p.terminate()

    @staticmethod
    def isAppRunning(process_name):
        return ProcessNotifier.isRunning(process_name)

    @staticmethod
    def getAppList(force_update = False):
        """ returns app_detail = (exec_path, icon_path)"""
        if force_update:
            AppProvider.apps = AppProvider.appDetails()
        return AppProvider.apps

    @staticmethod
    def appDetails():
        """ return the appropriate app details in format: (exec_path, icon_path)"""
        if not APP_PATH_REGEX:
            return []
        if OS_NAME == "Linux":
            return AppProvider.linuxAppDetails()
        return []

    @staticmethod
    def linuxGetIcon(icon_name):
        if os.path.isfile(icon_name):
            return icon_name
        icon_theme = Gtk.IconTheme.get_default()
        icon = icon_theme.lookup_icon(icon_name, 48, 0)
        if icon:
            return icon.get_filename()
        else:
            # print icon_name, " not found"
            return None

    @staticmethod
    def linuxAppDetails():
        """ get linux desktop file details """
        files = []
        # probe .desktop files
        for filename in glob.glob(APP_PATH_REGEX):
            de = DesktopEntry(filename)
            exec_path = de.getExec().split(" ")[0]

            if exec_path in APP_BLACK_LIST:
                continue

            icon_path = AppProvider.linuxGetIcon(de.getIcon())
            files.append((exec_path, icon_path))
        return files
