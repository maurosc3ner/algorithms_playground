
class nodo:
    def __init__(self,value):
        super().__init__()
        self.item=value
        self.sig=None

class stackLL:
    def __init__(self):
        super().__init__()
        self.cabeza=None
        self.cola=None
        self.N=0
    
    def tamano(self):
        return self.N
    
    def vacia(self):
        return (self.tamano()==0)
    
    def apilar(self,value):
        self.N+=1
        nodoAnt=self.cabeza
        self.cabeza=nodo(value)
        self.cabeza.sig=nodoAnt
        # inicializacion de la cola
        if(nodoAnt==None):
            self.cola=self.cabeza
    
    def extraer(self):
        if(self.cabeza!=None):
            self.N-=1
            dato=self.cabeza.item
            self.cabeza=self.cabeza.sig
            if(self.cabeza==None):
                self.cola=None
            return dato
        return -1

    def atravesar(self):
        temp=self.cabeza
        micadena=""
        while(temp):
            micadena+=str(temp.item)+";"
            temp=temp.sig
        print(micadena)

programa=stackLL()
print(programa.vacia())
print(programa.tamano())
programa.apilar(1)
print(programa.vacia())
print(programa.tamano())

programa.extraer()
print(programa.vacia())
print(programa.tamano())

programa.apilar(1)
programa.apilar(2)
programa.apilar(3)
print(programa.vacia())
print(programa.tamano())
programa.atravesar()

print(programa.extraer())
print(programa.extraer())
print(programa.extraer())
print(programa.vacia())
print(programa.tamano())
programa.atravesar()

print(programa.extraer())