# write a program that takes three integer command-line arguments and prints equal if all three are equal,
# and not equal otherwise
# python ex1.1.3.py 
import sys


class ex1_1_3:

    def main(self):
        n1=int(input('Numero 1:'))
        n2=int(input('Numero 2:'))
        n3=int(input('Numero 3:'))
        # print(n1)
        if( n1==n2 & n2==n3): print("Digitos iguales")
        else: print("Digitos no iguales")


programa=ex1_1_3()

programa.main()