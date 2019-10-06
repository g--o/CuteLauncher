import cairocffi as cairo

# import gi
from gi import require_version
require_version('Gtk', '3.0')
require_version('Wnck', '3.0')
# import gtk
import os
from gi.repository import Gtk, Gdk, GdkPixbuf, GLib, Wnck

OS_NAME = os.uname()[0]
APP_ICON_DIR = None
APP_ENTRY_DIR = None
APP_ENTRY_REGEX = None

if OS_NAME == "Linux":
    APP_ENTRY_DIR = "/usr/share/applications"
    APP_ENTRY_REGEX = "*.desktop"
    from xdg.DesktopEntry import DesktopEntry
elif OS_NAME == "Windows":
    raise Exception("Windows not supported yet")
elif OS_NAME == "Mac OS":
    raise Exception("Mac OS not supported yet")
else:
    raise Exception("Unsupported OS")

APP_PATH_REGEX = os.path.join(APP_ENTRY_DIR, APP_ENTRY_REGEX)
