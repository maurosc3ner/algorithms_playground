#la bolsa es una cola pero sin la posibilidad de remover


class bagLista:
    def __init__(self):
        super().__init__()
        self.bag=list()
    
    def agregarItem(self,item):
        self.bag.append(item)

    def tamano(self):
        return len(self.bag)

    def vacia(self):
        return (self.tamano()==0)
    # iterador custom del objeto bag
    def __iter__(self):
        return iter(self.bag)
    


programa=bagLista()
print(programa.tamano(), programa.vacia())
for i in range(1,5):
    programa.agregarItem(i)
print(programa.tamano(), programa.vacia())

promedio=0
N=programa.tamano()
for item in programa:
    print(item)
    promedio+=item

print("media {}".format(promedio/N))