
from Config import *
from Images import *

from Xlib import display

def mousepos():
    """mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib)."""
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]

class Clickable(Gtk.EventBox):
    SIZE = (64, 64)

    def __init__(self, clicked_fn = None):
        super(Clickable, self).__init__()
        self.clicked_fn = clicked_fn
        self.connect("button_press_event", self.clicked_fn)
        self.connect("motion_notify_event", self.motion_notify_event)

    def motion_notify_event(self, widget, event):
        x, y = mousepos()
        parent_window = self.get_parent_window()
        geo = parent_window.get_geometry()
        sx,sy = geo.width, geo.height
        parent_window.move(x - sx/2, y - sy/2)

class LabelButton(Gtk.Button):
    def __init__(self, label = "", clicked_fn = None):
        super(LabelButton, self).__init__()
        self.set_label(label)
        self.clicked_fn = clicked_fn
        self.connect("clicked", self.clicked_fn)

class ImageButton(Clickable):
    def __init__(self, image_path = IMG_APP_DEFAULT, clicked_fn = None):
        super(ImageButton, self).__init__(clicked_fn)
        image = image_from_file(image_path, Clickable.SIZE)
        # set the image & clean label
        self.add(image)
