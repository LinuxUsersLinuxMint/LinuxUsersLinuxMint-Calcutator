#!/usr/bin/python3
"Copyright© 2023 LinuxUsersLinuxMint"
"Python Calcutator Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır."
"Python Calcutator All Rights Reserved under the GPL(General Public License)."
"Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"
"A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"

command=input('calc> ')
about="Python Calcutator CLI(Command Line Interface / Komut Satırı Arayüzü) LICENCE=GPL2"

if command=="calc":
    print("calc> Transactions You Can Enter: ")
    print("collect\nExtraction\n\Impact\nDivide\nPercentage\nabout")
    number1=input('{0} Enter The 1st number: '. format(command))
    number2=input('{0} Enter The 2st number: '. format(command))
    process=input('{0} Enter the Transaction You Want to Perform: '. format(command))
    addition=float(number1)+float(number2)
    subraction=float(number1)-float(number2)
    multiplication=float(number1)*float(number2)
    division=float(number1)/float(number2)
    Percentage=float(number1)%float(number2)
    if process=="Addition": 
       print("{0} + {1} = {2}". format(number1,number2,addition))  
    elif process=="Subraction":
       print("{0} - {1} = {2}". format(number1,number2,subraction))
    elif process=="Multiplication":
       print("{0} * {1} = {2}". format(number1,number2,multiplication))
    elif process=="Division":
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
   print("Version: 0.2 (Last Updated September 17 , 2023 , 14:43)")
elif command=="licence":
   print("This Software is protected under the GPL2 license")
else:
   print("Invalid Command!")
