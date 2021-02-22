# una cola o Queue es fifo first input (primero en llegar) first output (primero en ser atendido)
# como una cola bancaria comun y corriente

import sys

class colaLista:
    def __init__(self):
        self.micola=list()

    def tamano(self):
        return len(self.micola)

    def estaVacia(self):
        return (len(self.micola)==0)

    def encolar(self,value):
        self.micola.append(value)

    def desencolar(self):
        if(not(self.estaVacia())):
            return self.micola.pop(0)

    def __iter__(self):
        return iter(self.micola)

q=colaLista()
# si es entrada por archivo 
# file1=open("...","r")
# si es entrada por stdin
pipe=sys.stdin.readlines()
kth=int(sys.argv[1])
# print(kth)
for line in pipe:
    # print(line)
    q.encolar(line.strip())

print(kth,q.tamano(),q.micola)

if(kth<=q.tamano()):
    for i in range(0,kth):
        print(i,q.desencolar())
    print(q.desencolar())