# Ilustra la clase minima de listas enlazadas, sus nodos
# y como recorrerlas

class nodo:
    def __init__(self,value):
        super().__init__()
        self.item=value
        self.next=None


class ListaEnlazada:
    # en python todos los atributos son publicos por defecto
    def __init__(self):
        super().__init__()
        self.cabeza=None

    # def agregar(self,nodo):


    def atravesar(self):
        temp=self.cabeza
        while(temp):
            print(temp.item)
            temp=temp.next

programa=ListaEnlazada()
programa.atravesar()
#agregar primer elemento
programa.cabeza=nodo(1)
nodo2=nodo(2)
nodo3=nodo(3)
programa.atravesar()

programa.cabeza.next=nodo2
programa.atravesar()

nodo2.next=nodo3
programa.atravesar()

