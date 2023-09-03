#!/usr/bin/python3
"Copyright© 2023 LinuxUsersLinuxMint"
"Python Calcutator Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır."
"Python Calcutator All Rights Reserved under the GPL(General Public License)."
"Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"
"A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"

command=input('calc> ')
about= "Python Calcutator CLI(Command Line Interface) LICENCE=GPL"
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
       print("CONCLUSION=", format(collect))  
    if process=="Extraction":
       print("CONCLUSION=", format(Extraction))
    if process=="Impact":
       print("CONCLUSION=", format(Impact))
    if process=="Divide":
       print("CONCLUSION=", format(Divide))
    if process=="Percentage":
       print("CONCLUSION=", format(Percentage))
if command=="about":
   print(about)
if command=="exit":
   exit()
if command=="help":
   print("Python calc Help")
   print("\n Command: calc , about , help , exit")