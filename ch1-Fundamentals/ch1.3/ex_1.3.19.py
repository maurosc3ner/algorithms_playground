# las linked list usan dos clases, una para nodo y otra para la lista de nodos
# ademas tienen dos referencias la cabeza y la cola
# si se hace como una cola, entonces 

class nodo:
    def __init__(self,item):
        super().__init__()
        self.item=item
        self.sig=None

class listaEnlazada:
    def __init__(self):
        super().__init__()
        self.cabeza=None
        self.cola=None
        self.N=0
    
    def tamano(self):
        return self.N
    
    def estaVacia(self):
        return (self.N==0)

    def agregar(self,value): # funciona como una cola, agregamos al final
        nodoAnt=self.cola
        self.cola=nodo(value)
        if(self.estaVacia()):
            self.cabeza=self.cola
        else:
            nodoAnt.sig=self.cola
        self.N+=1

    def eliminarCabeza(self):
        if(not(self.estaVacia())):
            nodoAnt=self.cabeza
            self.cabeza=self.cabeza.sig
            self.N-=1
            if(self.estaVacia()):
                self.cola=None
            return nodoAnt

    def recorrer(self):
        temp=self.cabeza
        cadena=""
        while(temp):
            cadena+=str(temp.item)+";"
            temp=temp.sig
        print(cadena)

    #ex_1.3.19
    def eliminarUltimo(self):
        temp=self.cabeza
        if(self.tamano()>1):
            while(temp.sig.sig):
                temp=temp.sig
            nodoAnt=temp.sig
            temp.sig=None
            self.N-=1
            return nodoAnt
        elif(self.tamano()==1):
            nodoAnt=self.cabeza
            self.cabeza=None
            self.cola=None
            self.N-=1
            return nodoAnt
        else:
            return -1


q=listaEnlazada()
q.agregar(1)
q.agregar(2)
q.agregar(3)
q.recorrer()

q.eliminarUltimo()
q.recorrer()
q.eliminarUltimo()
q.recorrer()
q.eliminarUltimo()
q.recorrer()

q.agregar(1)
q.agregar(2)
q.agregar(3)
q.agregar(4)
q.recorrer()
q.eliminarUltimo()
q.eliminarCabeza()
q.recorrer()