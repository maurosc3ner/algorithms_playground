

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

pila=pilaLista()
N=0
while(N<10):
    pila.apilar(int(N+1))
    N+=1

print(pila.mipila)
print(pila.peek())