
# TaskKiller v1
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to use](#setup)
* [How the code works](#How-the-code-works)

## General info
Python script to stop/kill background tasks and services that consume too much CPU power, memory or bandwidth with just one click.

### The problem
Some Tasks/Services in Win10 and Win7 auto-run on the computer and start consuming the computer recourses. We usually head over to Task Manager and manually stop them one by one. But sometimes they auto-restart and you can't simply prevent the auto-start for some reason.

_In this screenshot "Delivery Optimization" Service and "Microsoft Office Click-to-Run" are eating my internet connection in a time where I need the full internet bandwidth_
![Screenshot_Before](https://github.com/Abdoo-mayhob/TaskKiller/blob/main/Screenshot_Before.png)

### The solution
We basically automated the "go over to task manager and kill each process/service one by one" part. It's now just one click and python does the rest for us. 

_In this screenshot "Delivery Optimization" Service and "Microsoft Office Click-to-Run" got stopped along with some other process I defined earlier in TaskKiller_v1.py . Thus freeing up CPU usage, Ram and internet usage_
![Screenshot_After](https://github.com/Abdoo-mayhob/TaskKiller/blob/main/Screenshot_After.png)

## Technologies
Project is created with:
* psutil
* subprocess
* ctypes, sys

## How to use
There are 2 files, the py file is the main python code, and the bat file is just a batch file that the user may use to run the script by just clicking it, or maybe to run the script on startup if moved to windows startup folder.

In the py file the user can add the programs and services names wanted to be stopped.
You can get the service name by hitting (win+r) and typing services.msc and pressing enter, then search for the service you wish to stop and right click it then hit properties. The service name will be listed at the top, copy it and paste it as a string in the list ```list_of_services_to_kill ```. 
You can get the program name by right clicking it form the task manager then hitting properties. Add it to ```list_of_programs_to_kill``` as string, don't forget the .exe .

####The code is tested on Win10 and Win7.


## How the code works
First, the code checks if the python script has admin privileges. If no then re-run the script with admin privileges.
The rest of the code is self explanatory.
