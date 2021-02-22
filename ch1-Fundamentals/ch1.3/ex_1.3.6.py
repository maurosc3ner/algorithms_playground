class pilaLista:
    def __init__(self):
        super().__init__()
        self.mipila=list()
    
    def tamano(self):
        return len(self.mipila)

    def vacia(self):
        return (len(self.mipila)==0)
    
    def apilar(self,value):
        self.mipila.append(value)

    def desapilar(self):
        return self.mipila.pop()

    def __iter__(self):
        return iter(self.mipila)


class colaLista:
    def __init__(self):
        self.micola=list()

    def tamano(self):
        return len(self.micola)

    def vacia(self):
        return (len(self.micola)==0)

    def encolar(self,value):
        self.micola.append(value)

    def descolar(self):
        if(not self.vacia()):
            return self.micola.pop(0)

    def __iter__(self):
        return iter(self.micola)

pila=pilaLista()
cola=colaLista()
N=0
while(N<10):
    #conversor base 10 a base 2
    pila.apilar(int(N))
    cola.encolar(int(N))
    N+=1

print(pila.mipila)
print(cola.micola)

pila=pilaLista()

while(not cola.vacia()):
    pila.apilar(cola.descolar())
print(pila.mipila)
while(not pila.vacia()):
    cola.encolar(pila.desapilar())

print(cola.micola)
# reversa la cola al extraer el ultimo elemento de la pila