#primero en llegar (enqueue) primero en salir (dequeue)


class colaLista:
    # en python el constructor se define __init__
    def __init__(self):
        super().__init__()
        self.cola=list()
    
    def encolar(self,item):
        self.cola.append(item)

    #las colas si permiten borrar/atender elementos pero siempre el primer elemento
    def decolar(self):
        return self.cola.pop(0)
    
    def tamano(self):
        return len(self.cola)

    def vacia(self):
        return (self.tamano()==0)
    
    # el iterador se define __iter__
    def __iter__(self):
        return iter(self.cola)

    def get(self):
        return self.cola
miCola=colaLista()

for i in range(1,6):
    miCola.encolar(i)
    print(miCola.get())

for item in miCola:
    print(item)

print(miCola.get())
print(miCola.vacia())
N=miCola.tamano()
for i in range(0,N):
    print(miCola.decolar())

print(miCola.get())
print(miCola.vacia())
