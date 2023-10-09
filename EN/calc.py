#!/usr/bin/python3
import os
from colorama import Fore, init
init(autoreset=True)
process=int(0)
# Copyright© 2023 LinuxUsersLinuxMint
# Python Calcutator Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# Python Calcutator All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
print("******************************************************")
print("*** Welcome to Python-Calcutator 0.2.7 Program     ***")
print("""*** Options:                                       ***
***                                                ***
*** Enter the Command you want to choose...        ***
***                                                ***
*** 1. calc                                        ***
*** 2. about                                       ***
*** 3. exit                                        ***
*** 4. help                                        ***
*** 5. git-address                                 ***
*** 6. ver                                         ***
*** 7. licence                                     ***
*** 8. Thank                                       ***
******************************************************""")
command=str(input(Fore.LIGHTBLUE_EX +'calc> '))
os.system("clear")
about="Python Calcutator CLI(Command Line Interface / Komut Satırı Arayüzü) LICENCE=GPL2"
selected_transaction=str(Fore.LIGHTBLUE_EX+"None")
if command=="calc":
   print("""*** Transactions you can enter:     ***
         Selected Transaction={0}""". format(selected_transaction))
   print("""
1.   Addition
2.   Subraction
3.   Multiplication
4.   Division
5.   Percentage""")
   process=str(input('calc> Enter the Number of the Transaction You Want to Select: '))
   selected_transaction=process
   os.system("clear")
   print(Fore.LIGHTBLUE_EX+"""calc> Selected Transaction: 
         Selected Transaction={0}""". format(selected_transaction))
   number1=float(input('calc> Enter The 1st Number: '))
   number2=float(input('calc> Enter The 2st Number: '))
   os.system("clear")
if process=="1": 
     print("{0} + {1} = {2}". format(number1,number2,number1+number2))  
elif process=="2":
     print("{0} - {1} = {2}". format(number1,number2,number1-number2))
elif process=="3":
     print("{0} * {1} = {2}". format(number1,number2,number1*number2))
elif process=="4":
     print("{0} / {1} = {2}". format(number1,number2,number1/number2))
elif process=="5":
     print("{0} % {1} = {2}". format(number1,number2,number1%number2))
else:
     print("Invalid Process!")
     if command=="about":
          print(about)
     elif command=="exit":
          exit()
     elif command=="help":
          print("Python calc Help")
          print("\n Command: calc , about , help , exit , git-address , web-site , ver , licence , Thank")
     elif command=="git-address":
          print("Github Link: https://github.com/LinuxUsersLinuxMint")
     elif command=="web-site":
          print("linuxuserslinuxmint.github.io")
     elif command=="ver":
          print("Version: 0.2.7 (Last Updated on October 6, 2023, 18:03)")
     elif command=="licence":
          print("This Software is protected under the GPL2 license")
     elif command=="Thank":
          print("Thank You for Using Python-Calcutator.")
     else:
          print("Invalid Command!")