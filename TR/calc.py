#!/usr/bin/python3
import os
from colorama import Fore, init
init(autoreset=True)
"Copyright© 2023 LinuxUsersLinuxMint"
"Python Calcutator Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır."
"Python Calcutator All Rights Reserved under the GPL(General Public License)."
"Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"
"A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"
print("******************************************************")
print("*** Python-Calcutator 0.2.5 Programına Hoşgeldiniz ***")
print("""*** Seçenekler:                                    ***

*** Seçmek istediğiniz Komutu Giriniz...           ***

1. calc
2. about
3. exit
4. help
5. git-address
6. ver
7. licence""")
command=str(input(Fore.LIGHTBLUE_EX +'calc> '))
os.system("clear")
about="Python Hesap Makinesi CLI(Command Line Interface / Komut Satırı Arayüzü) LICENCE=GPL2"
secilen_islem=str(Fore.LIGHTBLUE_EX+"None")
if command=="calc":
   print("""calc> Girebileceğiniz işlemler: 
         Seçilen İşlem={0}""". format(secilen_islem))
   print("""
1.   Toplama
2.   Çıkarma
3.   Çarpma
4.   Bölme
5.   Yüzde""")
   islem=input('calc> Seçmek İstediğiniz İşlemin Numarasını Giriniz: ')
   os.system("clear")

   secilen_islem=islem
   print("""calc> Seçilen İşlem: 
         Seçilen İşlem={0}""". format(secilen_islem))
   sayi1=input('calc> 1. sayiyi giriniz: ')
   sayi2=input('calc> 2. sayiyi giriniz: ')
   os.system("clear")
   top=float(sayi1)+float(sayi2)
   cık=float(sayi1)-float(sayi2)
   carp=float(sayi1)*float(sayi2)
   bol=float(sayi1)/float(sayi2)
   yuzde=float(sayi1)%float(sayi2)
   if islem=="1": 
      print("{0} + {1} = {2}". format(sayi1,sayi2,top))  
   elif islem=="2":
       print("{0} - {1} = {2}". format(sayi1,sayi2,cık))
   elif islem=="3":
       print("{0} * {1} = {2}". format(sayi1,sayi2,carp))
   elif islem=="4":
       print("{0} / {1} = {2}". format(sayi1,sayi2,bol))
   elif islem=="5":
       print("{0} % {1} = {2}". format(sayi1,sayi2,yuzde))
else:
     print("Geçersiz İşlem")
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
     print("Sürüm: 0.2.5 (Son Güncellenme Tarihi 1 Ekim , 2023 , 16:46)")
elif command=="licence":
     print("This Software is protected under the GPL2 license")
else:
     print("Geçersiz Komut")