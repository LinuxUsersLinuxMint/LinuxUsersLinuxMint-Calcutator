#!/usr/bin/python3
# Bu Program Python-Calcutator'u derlemek için oluşturulmuştur.
# This program was created to compile Python-Calcutator.

import os

operating_sys=str(input('Operating System (Windows/Linux/MacOS):   '))

if operating_sys=="Windows":
    usr=str(os.system("%users%"))
    ProgramPath=str(input('Program Path (C:\...) (EN/TR):   '))
    FileName=str(input('File Name: '))
    debugPath=str(ProgramPath)
    debug=os.system("cd {0}". format(debugPath))
    debugfile=os.system("pyinstaller --onefile {0}". format(FileName))
elif operating_sys=="Linux" or operating_sys=="MacOS":
    ProgramPath=str(input('Program Path (/...) (EN/TR):   '))
    FileName=str(input('File Name: '))
    debugPath=str(ProgramPath)
    debug=os.system("cd {0}". format(debugPath))
    debugfile=os.system("pyinstaller --onefile {0}". format(FileName))
else:
    print("Invalid Operating System...!")