
from Config import *
from Images import *

class Clickable(Gtk.EventBox):
    SIZE = (64, 64)

    def __init__(self, clicked_fn = None):
        super(Clickable, self).__init__()
        self.clicked_fn = clicked_fn
        self.connect("button_press_event", self.clicked_fn)

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
