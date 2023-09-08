#!/usr/bin/python3
command=input('calc> ')
comtxt="calc> "
about="Python Calcutator CLI(Command Line Interface / Komut Satırı Arayüzü) LICENCE=GPL2"
number1=input('{0} Enter The 1st number: '. format(comtxt))
number2=input('{0} Enter The 2st number: '. format(comtxt))
process=input('{0} Enter the Transaction You Want to Perform: '. format(comtxt))
addition=float(number1)+float(number2)
subraction=float(number1)-float(number2)
multiplication=float(number1)*float(number2)
division=float(number1)/float(number2)
Percentage=float(number1)%float(number2)