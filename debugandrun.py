#!/usr/bin/python3
# Bu Program Python-Calcutator'u derlemek için oluşturulmuştur.
# This program was created to compile Python-Calcutator.

import platform, os
import time

operating_sys = platform.system()

if operating_sys =="Windows" or operating_sys == "windows" or operating_sys == "NT" or operating_sys == "nt":
    users_name=str(input('Enter The Users Name: '))
    ProgramPath_Ws=str(input('Version (EN/TR):   '))
    debug=os.system("cd {0}". format(ProgramPath_Ws))
    debugfile=os.system("pyinstaller --onefile calc.py")

elif operating_sys =="Linux" or operating_sys == "linux" or operating_sys=="MacOS" or operating_sys == "macOS" or operating_sys == "darwin" or operating_sys == "Darwin":
    users_nm=str(input('Enter The Users Name: '))
    ver_name=str(input('Version (EN/TR): '))
    ProgramPath=str("/home/{0}/Desktop/Python-Calcutator-main/{1}/". format(users_nm,ver_name))
    debugPath=str(os.system("cd /home/{0}/Desktop/Python-Calcutator-main/{1}". format(users_nm,ver_name)))
    time.sleep(2)
    print("[DEBUGANDRUN]: The Program is Preparing to Compile...")
    time.sleep(2)
    print("[DEBUGANDRUN]: Checking Program Information...")
    users_list=str(list(users_nm))
    ver_list=str(list(ver_name))
    ProgramPath_list=str(list(ProgramPath))
    debugPath_list=str(list(debugPath))
    time.sleep(2)
    print("[DEBUGANDRUN]: Program Information Listed...\n{0}\n{1}\n{2}\n{3}". format(users_list,ver_list,ProgramPath_list,debugPath_list))
    time.sleep(2)
    print("[DEBUGANDRUN] Program Compiler is Preparing...")
    time.sleep(2)
    print("[DEBUGANDRUN]: Compiling the Program...")
    dbg=os.system("pyinstaller --onefile calc.py")
    dbg
    time.sleep(2)
    print("[DEBUGANDRUN]: Compilation Process is Completed...")

else:
    print("Invalid Operating System...!")