import os, sys
import psutil
from win32 import win32gui
import win32.lib.win32con as win32con
from win32.win32gui import FindWindow

def read_pids_from_file(filename):
    with open(filename, "r") as file:
        pids = [int(line.strip()) for line in file]
    os.remove(filename)
    return pids

def terminate_child_processes(child_pids):
    for pid in child_pids:
        try:
            process = psutil.Process(pid)
            print(pid)
            os.system("taskkill /F /T /PID "+ str(pid))
        except:
            pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    pids_to_parse = sys.argv[1]
    pids = [int(item) for item in pids_to_parse.split()]

    script_path = os.path.abspath(__file__)
    script_dir = os.path.dirname(script_path)
    os.chdir(script_dir)
    ayaklandirici = read_pids_from_file("pid.txt")[0]

    while(psutil.pid_exists(ayaklandirici)):
        pass
    
    terminate_child_processes(pids)
