import sys

# ordena 3 numeros 

class ex_1_1_26:
    def ordenar3(self,a,b,c):
        if(a>b):
            t=a
            a=b
            b=t
        if(a>c):
            t=a
            a=c
            c=t
        if(b>c):
            t=b
            b=c
            c=t

        print (a,b,c)

    def main(self):
        a=int(sys.argv[1])
        b=int(sys.argv[2])
        c=int(sys.argv[3])
        print(self.ordenar3(a,b,c))

programa=ex_1_1_26()
programa.main()