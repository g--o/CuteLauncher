from Config import *
import psutil

class ProcessNotifier(object):
    screen = Wnck.Screen.get_default()
    open_procs = {}

    @staticmethod
    def getProcNameByPID(pid):
        return psutil.Process(pid).name()

    @staticmethod
    def isRunning(proc_name):
        return ProcessNotifier.open_procs.has_key(proc_name)

    @staticmethod
    def update():
        ProcessNotifier.open_procs = ProcessNotifier.getOpenProcs()

    @staticmethod
    def getOpenProcsCached():
        return ProcessNotifier.open_procs

    @staticmethod
    def getOpenProcs():
        ProcessNotifier.screen.force_update()
        wins = ProcessNotifier.screen.get_windows()
        procs = {}

        try:
            for win in wins:
                if win.get_pid() != os.getpid(): # if its not us
                    procs[ ProcessNotifier.getProcNameByPID(win.get_pid()) ] = win
        except:
            print "[ProcessNotifier] failed to update, removal in process?"

        return procs

    @staticmethod
    def getActiveProc():
        ProcessNotifier.getProcNameByPID(ProcessNotifier.screen.get_active_window.pid)