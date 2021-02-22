# la pila o stack es lifo last input first output a diferencia de la cola of FIFO

class pilaLista:
    def __init__(self):
        super().__init__()
        self.mipila=list()
    
    def tamano(self):
        return len(self.mipila)

    def vacia(self):
        return (len(self.mipila==0))
    
    def apilar(self,value):
        self.mipila.append(value)

    def desapilar(self):
        return self.mipila.pop()

    def __iter__(self):
        return iter(self.mipila)

    def peek(self):
        return self.mipila[self.tamano()-1]

    def copy(self,pila):
        for i  in pila:
            self.apilar(i)


pila1=pilaLista()
N=0
while(N<10):
    pila1.apilar(int(N+1))
    N+=1

print(pila1.mipila)
pila2=pilaLista()
pila2.copy(pila1)
print(pila2.mipila)
# for i in pila1:
#     print(i)
#     pila2.apilar()