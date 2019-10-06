
from Config import *
from LauncherLayout import *
import Logger

# Launcher window
class LauncherWindow(Gtk.Window):
    def __init__(self, layout_maker = default_layout, layout = None):
        super(LauncherWindow, self).__init__()

        # set up window
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(0)
        self.set_decorated(False)
        self.set_resizable(False)

        # set layout
        if layout:
            self.layout_window = layout
        else:
            self.layout_window = layout_maker()

        self.screen = self.get_screen()
        self.visual = self.screen.get_rgba_visual()
        if self.visual != None and self.screen.is_composited():
            self.set_visual(self.visual)
        else:
            Logger.log("[Compositor] Advance graphics aren't supported!")

        # set up layout
        self.add(self.layout_window)

        # set up custom events
        self.set_app_paintable(True)
        self.connect("draw", self.area_draw)
        self.show_all()

    def area_draw(self, widget, cr):
        cr.set_source_rgba(.0, .0, .0, .0)
        cr.set_operator(cairo.OPERATOR_SOURCE)
        cr.paint()
        cr.set_operator(cairo.OPERATOR_OVER)

    def get_screen_size(self):
        screen_width = self.screen.get_width()
        screen_height = self.screen.get_height()
        return (screen_width, screen_height)
