#!/usr/bin/python3
"Copyright© 2023 LinuxUsersLinuxMint"
"Python Calcutator Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır."
"Python Calcutator All Rights Reserved under the GPL(General Public License)."
"Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"
"A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"

command=input('calc> ')
about= "Python Calcutator CLI(Command Line Interface) LICENCE=GPL2"
if command=="calc":
    print("calc> Transactions You Can Enter: ")
    print("collect\nExtraction\n\Impact\nDivide\nPercentage\nabout")
    number1=input('calc> Enter the 1st number: ')
    number2=input('calc> Enter the 2nd number: ')
    process=input('calc> Enter the action you want to perform: ')
    collect=float(number1)+float(number2)
    Extraction=float(number1)-float(number2)
    Impact=float(number1)*float(number2)
    Divide=float(number1)/float(number2)
    Percentage=float(number1)%float(number2)
    if process=="collect": 
       print("{0} + {1} = {2}". format(number1,number2,collect))  
    elif process=="Extraction":
       print("{0} - {1} = {2}". format(number1,number2,Extraction))
    elif process=="Impact":
       print("{0} * {1} = {2}". format(number1,number2,Impact))
    elif process=="Divide":
       print("{0} / {1} = {2}". format(number1,number2,Divide))
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
   print("Version: 0.1.5.5 (Last Updated September 6 , 2023 , 22:22)")
elif command=="licence":
   print("This Software is protected under the GPL2 license")
else:
   print("Invalid Command!")