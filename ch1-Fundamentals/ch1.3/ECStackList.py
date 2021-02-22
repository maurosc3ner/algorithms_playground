
class pilaLista:
    # constructor __init__
    def __init__(self):
        super().__init__()
        self.pila=list()

    def apilar(self,item):
        self.pila.append(item)

    def extraer(self):
        return self.pila.pop()
    
    def tamano(self):
        return len(self.pila)

    def vacia(self):
        return (self.tamano==0)
    
    def __iter__(self):
        return iter(self.pila)

    def get(self):
        return self.pila

miPila=pilaLista()

for i in range(1,6):
    miPila.apilar(i)
    print(miPila.get())

N=miPila.tamano()
# iterate
for item in miPila:
    print(item)


for i in range(0,N):
    miPila.extraer()
    print(miPila.get())
