#!/usr/bin/python3
import os
from colorama import Fore, init
init(autoreset=True)
# Copyright© 2023 LinuxUsersLinuxMint
# Python Calcutator Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır.
# Python Calcutator All Rights Reserved under the GPL(General Public License).
# Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
# A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint
print("******************************************************")
print("*** Python-Calcutator 0.2.7 Programına Hoşgeldiniz ***")
print("""*** Seçenekler:                                    ***
***                                                ***
*** Seçmek istediğiniz Komutu Giriniz...           ***
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
about="Python Hesap Makinesi CLI(Command Line Interface / Komut Satırı Arayüzü) LICENCE=GPL2"
secilen_islem=str(Fore.LIGHTBLUE_EX+"None")
if command=="calc":
   print("""*** Girebileceğiniz işlemler:     ***
         Seçilen İşlem={0}""". format(secilen_islem))
   print("""
1.   Addition
2.   Subraction
3.   Multiplication
4.   Division
5.   Percentage""")
   process=str(input('calc> Seçmek İstediğiniz İşlemin Numarasını Giriniz: '))
   secilen_islem=process
   os.system("clear")
   print(Fore.LIGHTBLUE_EX+"""calc> Seçilen İşlem: 
         Seçilen İşlem={0}""". format(secilen_islem))
   number1=float(input('calc> Enter The 1st Number: '))
   number2=float(input('calc> Enter The 2st Number: '))
   os.system("clear")
if islem=="1": 
     print("{0} + {1} = {2}". format(sayi1,sayi2,sayi1+sayi2))  
elif islem=="2":
     print("{0} - {1} = {2}". format(sayi1,sayi2,sayi1-sayi2))
elif islem=="3":
     print("{0} * {1} = {2}". format(sayi1,sayi2,sayi1*sayi2))
elif islem=="4":
     print("{0} / {1} = {2}". format(sayi1,sayi2,sayi1/sayi2))
elif islem=="5":
     print("{0} % {1} = {2}". format(sayi1,sayi2,sayi1%sayi2))
else:
     print("Geçersiz İşlem!")
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
          print("Sürüm: 0.2.7 (Son Güncellenme Tarihi 6 Ekim , 2023 , 18:03)")
     elif command=="licence":
          print("This Software is protected under the GPL2 license")
     elif command=="Thank":
          print("Thank You for Using Python-Calcutator.")
     else:
          print("Invalid Command!")