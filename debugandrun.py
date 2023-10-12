#!/usr/bin/python3
# Bu Program Python-Calcutator'u derlemek için oluşturulmuştur.
# This program was created to compile Python-Calcutator.

import os
import time

operating_sys=str(input('Operating System (Windows/Linux/MacOS): '))

if operating_sys=="Windows":
    users_name=str(input('Enter The Users Name: '))
    ProgramPath_Ws=str(input('Version (EN/TR):   '))
    debug=os.system("cd {0}". format(ProgramPath_Ws))
    debugfile=os.system("pyinstaller --onefile calc.py")
elif operating_sys=="Linux" or operating_sys=="MacOS":
    users_nm=str(input('Enter The Users Name: '))
    ver_name=str(input('Version (EN/TR): '))
    ProgramPath=str("/home/{0}/Desktop/Python-Calcutator-main/{1}/". format(users_nm,ver_name))
    debugPath=str(os.system("cd /home/{0}/Desktop/Python-Calcutator-main/{1}". format(users_nm,ver_name)))
    time.sleep(2)
    print("[DEBUGANDRUN]: Program Derlenmeye Hazırlanıyor...")
    time.sleep(2)
    print("[DEBUGANDRUN]: Program Bilgileri Kontrol Ediliyor...")
    users_list=str(list(users_nm))
    ver_list=str(list(ver_name))
    ProgramPath_list=str(list(ProgramPath))
    debugPath_list=str(list(debugPath))
    time.sleep(2)
    print("[DEBUGANDRUN]: Program Bilgileri Listeleniyor...\n{0}\n{1}\n{2}\n{3}". format(users_list,ver_list,ProgramPath_list,debugPath_list))
    time.sleep(2)
    print("[DEBUGANDRUN] Program Derleyicisi Hazırlanıyor...")
    global debugger,debugger_opt,debug_file
    debugger=str('pyinstaller')
    debugger_opt=str('--onefile')
    debug_file=str("calc.py")
    time.sleep(2)
    print("[DEBUGANDRUN]: Program Derleniyor...")
    dbg=os.system("{0} {1} {2}". format(debugger,debugger_opt,debug_file))
    time.sleep(2)
    print("[DEBUGANDRUN]: Derleme İşlemi Bitmiştir...")
else:
    print("Invalid Operating System...!")