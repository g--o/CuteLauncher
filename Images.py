
from Config import *

import os.path

def image_from_file(path, size = None):
    """ size - tuple of image size (width, height) """
    if (path is None or not os.path.isfile(path)):
        path = IMG_APP_DEFAULT

    image = Gtk.Image()

    if size:
        # create image widget
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(path, width=size[0], height=size[1],
                                                         preserve_aspect_ratio=False)
        image.set_from_pixbuf(pixbuf)
    else:
        image.set_from_file(path)
    return image

IMG_APP_DEFAULT = "./assets/app.png"
