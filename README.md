# TaskKiller v1
## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [How to use](#setup)
* [How the code works](#How-the-code-works)

## General info
Python script to stop/kill background tasks and services that consume too much CPU power, memory or bandwidth.
	
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

## How the code works
First, the code checks if the python script has admin privileges. If no then re-run the script with admin privileges.
The rest of the code is self explanatory.
