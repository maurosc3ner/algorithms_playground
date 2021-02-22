# La pila o stack es last input first output
# por tanto push y pop son normales a diferencia de la Cola

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
        self.mipila.pop()

    def __iter__(self):
        return iter(self.mipila)

pila=pilaLista()
N=50
while(N>0):
    #conversor base 10 a base 2
    pila.apilar(int(N%2))
    N=int(N/2)

print(pila.mipila)
pila.desapilar()
print(pila.mipila)