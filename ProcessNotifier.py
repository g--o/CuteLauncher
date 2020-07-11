import pyinotify

# Linux code
LINUX_DIR = "/proc"

class MyEventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print("File created:", event.pathname)

    def process_IN_OPEN(self, event):
        print("File opened::", event.pathname)

def start_watch():
    # Watch manager (stores watches, you can add multiple dirs)
    wm = pyinotify.WatchManager()
    # User's music is in /tmp/music, watch recursively
    wm.add_watch(LINUX_DIR, pyinotify.ALL_EVENTS, rec=True)

    # Previously defined event handler class
    eh = MyEventHandler()

    # Register the event handler with the notifier and listen for events
    notifier = pyinotify.Notifier(wm, eh)
    notifier.loop()
