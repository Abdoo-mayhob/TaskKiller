# TaskKiller v1
# MadeBy: AbDoO_
# 2020 - 3 - 14 23:24
#------------------------
# You need to pip install psutil first

list_of_programs_to_kill = [
    'OfficeClickToRun.exe',
    'opera_autoupdate.exe',
    'smartscreen.exe'
]

list_of_services_to_kill = [
    'DoSvc', # Delivery Optimization
    'BITS'   # Background Intelligent Transfer Service
]


def intro():
    print("TaskKiller v1")
    print("This Script Was Made By AbDoO_")
    print("2020 - 3 - 14 23:24")
    print("--------------------------------")


def Task_Killer():
    import psutil
    for proc in psutil.process_iter():
        try:
            if not "System" in str(proc.name):     # if the procces is not a system procces
                for i in list_of_programs_to_kill:
                    if  i in str(proc.name):
                        proc.kill()
                        print(i,' Killed  ')
        except Exception as e:
            print('Error:',e)

    print('Done !  Have Fun <>_<>  <3')


def Services_Stopper():
    import subprocess
    for ser in list_of_services_to_kill:
        args = ['sc', 'stop', ser]
        result = subprocess.run(args)
        print(result,'\n--------------------\n')


# Run this file as admin
import ctypes, sys
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False


if is_admin():
    intro()
    Task_Killer()
    Services_Stopper()
    x = input() # Pasue the screen
    
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

