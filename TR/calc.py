#!/usr/bin/python3
"Copyright© 2023 LinuxUsersLinuxMint"
"Python Calcutator Tüm Hakları GPL(Genel Kamu Lisansı) altında korunmaktadır."
"Python Calcutator All Rights Reserved under the GPL(General Public License)."
"Bu Yazılımın Bir Kopyası GİTHUB da yayınlanmaktadır Görüntülemek için: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"
"A Copy of This Software is published on GITHUB To view: https://github.com/LinuxUsersLinuxMint/LinuxUsersLinuxMint"

command=str(input('calc> '))
about="Python Hesap Makinesi CLI(Command Line Interface / Komut Satırı Arayüzü) LICENCE=GPL2"

if command=="calc":
   print("calc> Girebileceğiniz işlemler: ")
   print("top\ncık\n\carp\nbol\nyuzde\nabout")
   sayi1=input('{0} 1. sayiyi giriniz: '. format(command))
   sayi2=input('{0} 2. sayiyi giriniz: '. format(command))
   islem=input('{0} Gerçekleştirmek İstediğiniz İşlemi Giriniz: '. format(command))
   top=float(sayi1)+float(sayi2)
   cık=float(sayi1)-float(sayi2)
   carp=float(sayi1)*float(sayi2)
   bol=float(sayi1)/float(sayi2)
   yuzde=float(sayi1)%float(sayi2)
   if islem=="top": 
      print("{0} + {1} = {2}". format(sayi1,sayi2,top))  
   elif islem=="cık":
       print("{0} - {1} = {2}". format(sayi1,sayi2,cık))
   elif islem=="carp":
       print("{0} * {1} = {2}". format(sayi1,sayi2,carp))
   elif islem=="bol":
       print("{0} / {1} = {2}". format(sayi1,sayi2,bol))
   elif islem=="yuzde":
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
        print("Sürüm: 0.2 (Son Güncellenme Tarihi 17 Eylül , 2023 , 14:43)")
   elif command=="licence":
        print("This Software is protected under the GPL2 license")
   else:
        print("Geçersiz Komut")
