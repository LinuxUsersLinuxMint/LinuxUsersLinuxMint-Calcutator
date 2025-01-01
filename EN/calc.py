#!/usr/bin/python3
import os
from colorama import Fore, init
from Basic_Maths import *
init(autoreset=True)
process=int(0)
error_dialog = "Invalid Process/Command!"
"""Copyright© 2023-2025 LinuxUsersLinuxMint
Python Calcutator Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
Python Calcutator All Rights Reserved under the GPL(General Public License).
Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator
A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator """
print("*********************************************************************")
print("*** Welcome to LinuxUsersLinuxMint-Calcutator 0.3.3 Program       ***")
print("""*** Options:                                                      ***
***                                                               ***
*** Enter the Command you want to choose...                       ***
***                                                               ***
*** 1. calc                                                       ***
*** 2. about                                                      ***
*** 3. exit                                                       ***
*** 4. help                                                       ***
*** 5. git-address                                                ***
*** 6. ver                                                        ***
*** 7. licence                                                    ***
*** 8. Thank                                                      ***
*********************************************************************""")
command=str(input(Fore.LIGHTBLUE_EX +'calc> '))
os.system("clear")
about="Python Calcutator CLI(Command Line Interface) LICENCE=GPL2"
selected_transaction=str(Fore.LIGHTBLUE_EX+"None")
if command=="calc":
   print("""*** Transactions you can enter:     ***
         Selected Transaction={0}""". format(selected_transaction))
   print("""
1.   Addition
2.   Extraction
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
     addition(number1,number2,"Result: ")
elif process=="2":
     Extraction(number1,number2,"Result: ")
elif process=="3":
     Multiplication(number1,number2,"Result: ")
elif process=="4":
     Division(number1,number2,"Result: ", "Number cannot be zero in division!")
elif process=="5":
     Percentage(number1,number2,"Result: ")
else:
     error_msg()

if command=="about":
     print(about)
elif command=="exit":
     exit_select = input('Select the method to exit the program (0: Dialogue and Time entry, 1: Time entry only, 2: Dialogue entry only, 3: Normal exit (old style)): ')
     exit_select = int(exit_select)
     if exit_select == 0:
          userTime = input('After how many seconds should the program be closed?: ')
          userTime = int(userTime)
          exit_program_dialog_time("Exit program...", userTime)
     elif exit_select == 1:
          userTime = input('After how many seconds should the program be closed?: ')
          userTime = int(userTime)
          exit_program_time(userTime)
     elif exit_select == 2:
          exit_program_dialog("Exit program...")
     elif exit_select == 3:
          exit()
     else:
          error_msg()
elif command=="help":
     print("LinuxUsersLinuxMint-Calcutator Help")
     print("\n Command: calc , about , help , exit , git-address , web-site , ver , licence , Thank")
elif command=="git-address":
     print("Github Link: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint-Calcutator")
elif command=="web-site":
     print("https://linuxuserslinuxmint.github.io")
elif command=="ver":
     print("Version: 0.3.3 (Last Updated on Oct 25, 2024, 23:39)")
elif command=="licence":
     print("This Software is protected under the GPL2 license")
elif command=="Thank":
     print("Thank You for Using Python-Calcutator.")
else:
     error_msg()