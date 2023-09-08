#!/usr/bin/python3
from inputden import *
"Copyright© 2023 LinuxUsersLinuxMint"
"Python Calcutator Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır."
"Python Calcutator All Rights Reserved under the GPL(General Public License)."
"Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"
"A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"

if command=="calc":
    print("calc> Transactions You Can Enter: ")
    print("collect\nExtraction\n\Impact\nDivide\nPercentage\nabout")
    number1 , number2 , process
    if process=="collect": 
       print("{0} + {1} = {2}". format(number1,number2,addition))  
    elif process=="Extraction":
       print("{0} - {1} = {2}". format(number1,number2,subraction))
    elif process=="Impact":
       print("{0} * {1} = {2}". format(number1,number2,multiplication))
    elif process=="Divide":
       print("{0} / {1} = {2}". format(number1,number2,division))
    elif process=="Percentage":
       print("{0} % {1} = {2}". format(number1,number2,Percentage))
    else:
       print("Invalid Proccess!")
if command=="about":
   print(about)
elif command=="exit":
   exit()
elif command=="help":
   print("Python calc Help")
   print("\n Command: calc , about , help , exit , git-address , web-site , ver , licence")
elif command=="git-address":
   print("Github Link: https://github.com/LinuxUsersLinuxMint")
elif command=="web-site":
   print("linuxuserslinuxmint.github.io")
elif command=="ver":
   print("Version: 0.1.7 (Last Updated September 8 , 2023 , 18:08)")
elif command=="licence":
   print("This Software is protected under the GPL2 license")
else:
   print("Invalid Command!")