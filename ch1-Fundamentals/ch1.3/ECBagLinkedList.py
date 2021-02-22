

class nodo:
    def __init__(self,value):
        super().__init__()
        self.item=value
        self.sig=None

class BagLL:
    def __init__(self):
        super().__init__()
        self.cabeza=None
        self.N=0
    
    def tamano(self):
        return (self.N)
    
    def vacia(self):
        return (self.N==0)

    def agregar(self,value):
        self.N+=1
        nodoAnt=self.cabeza
        self.cabeza=nodo(value)
        self.cabeza.sig=nodoAnt

    def atravesar(self):
        temp=self.cabeza
        micadena=""
        while(temp):
            micadena+=str(temp.item)+";"
            temp=temp.sig
        return micadena


prog=BagLL()
print(prog.tamano())
print(prog.vacia())
prog.agregar(1)
print(prog.tamano())
print(prog.vacia())