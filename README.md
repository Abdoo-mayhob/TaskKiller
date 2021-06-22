# TaskKiller v1
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to use](#setup)
* [How the code works](#How-the-code-works)

## General info
Python script to stop/kill background tasks and services that consume too much CPU power, memory or bandwidth with just one click.

### The problem
Some Tasks/Services in Win10 and Win7 auto-run on the computer and start consuming the computer resourses. We usualy head over to Task Manager and manulay stop them one by one. But sometimes they auto-restart and you can't simply prevint the auto-start for some reason.

### The solution
We basicly automated the "go over to task manager and kill each proccess/sevice one by one" part. It's now just one click and python does the rest for us. 

## Technologies
Project is created with:
* psutil
* subprocess
* ctypes, sys

## How to use
There are 2 files, the py file is the main python code, and the bat file is just a batch file that the user may use to run the script by just clicking it, or maybe to run the script on startup if moved to windows startup folder.

In the py file the user can add the programsa and services names wanted to be stoped.
You can get the service name by hitting (win+r) and typing services.msc and pressing enter, then search for the service you wish to stop and right click it then hit properties. The service name will be listed at the top, copy it and paste it as a string in the list ```list_of_services_to_kill ```. 
You can get the program name by right clicking it form the task manager then hitting proerties. Add it to ```list_of_programs_to_kill``` as string, don't forget the .exe .

####The code is tested on Win10 and Win7.


## How the code works
First, the code checks if the python script has admin privileges. If no then re-run the script with admin privileges.
The rest of the code is self explanatory.
