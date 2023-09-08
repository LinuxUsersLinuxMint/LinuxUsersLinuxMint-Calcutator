#!/usr/bin/python3
command=input('calc> ')
comtxt="calc> "
about="Python Hesap Makinesi CLI(Command Line Interface / Komut Satırı Arayüzü) LICENCE=GPL2"
sayi1=input('{0} 1. sayiyi giriniz: '. format(comtxt))
sayi2=input('{0} 2. sayiyi giriniz: '. format(comtxt))
islem=input('{0} Gerçekleştirmek İstediğiniz İşlemi Giriniz: '. format(comtxt))
top=float(sayi1)+float(sayi2)
cık=float(sayi1)-float(sayi2)
carp=float(sayi1)*float(sayi2)
bol=float(sayi1)/float(sayi2)
yuzde=float(sayi1)%float(sayi2)