# ejemplo mas avanzado que incluye agregar un item al comienzo
# y remover al comienzo
class nodo:
    def __init__(self,value):
        super().__init__()
        self.item=value
        self.sig=None


class listaEnlazada:
    def __init__(self):
        super().__init__()
        self.cabeza=None
        self.ultimo=None
    
    def push(self,value):
        nodoAnt=self.cabeza
        self.cabeza=nodo(value)
        self.cabeza.sig=nodoAnt
        if(nodoAnt==None):
            self.ultimo=self.cabeza

    def extraer(self):
        self.cabeza=self.cabeza.sig
        if(self.cabeza==None):
            self.ultimo=None

    def atravesar(self):
        temp=self.cabeza
        string=""
        while(temp):
            string+=str(temp.item)+";"
            temp=temp.sig
            # print(temp.item)
        print(string)

programa=listaEnlazada()
programa.push(1)
programa.atravesar()
print(programa.ultimo.item)
programa.push(2)
programa.push(3)
programa.atravesar()
print(programa.ultimo.item)
programa.extraer() #3
programa.atravesar()
print(programa.ultimo.item)
programa.extraer() #2
programa.atravesar()
print(programa.ultimo.item)
programa.extraer() #1
programa.atravesar()
print(programa.ultimo.item)