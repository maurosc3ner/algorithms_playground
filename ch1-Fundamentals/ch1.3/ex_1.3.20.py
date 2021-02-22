#  incluye 1.3.20 y 1.3.21
class nodo:
    def __init__(self,value):
        super().__init__()
        self.item=value
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

    # como este es una cola, agregamos al final
    def agregar(self,value):
        nodoAnt=self.cola
        self.cola=nodo(value)
        if(self.estaVacia()):
            self.cabeza=self.cola
        else:
            nodoAnt.sig=self.cola
        # se aumenta solo al final
        self.N+=1

    def eliminarCabeza(self):
        if(not(self.estaVacia())):
            nodoAnt=self.cabeza
            self.cabeza=self.cabeza.sig
            self.N-=1
            if(self.estaVacia()):
                self.cola=None
            return nodoAnt

    # aqui la idea es revisar el penultimo
    def eliminarCola(self):
        temp=self.cabeza
        if(self.N>=1):
            while(temp.sig.sig):
                temp=temp.sig
            nodoAnt=self.cola
            temp.sig=None
            self.N-=1
        elif(self.N==1):
            nodoAnt=self.cabeza
            self.cabeza=None
            self.cola=None
            self.N-=1
        else:
            nodoAnt=-1
        return nodoAnt

    def recorrer(self):
        temp=self.cabeza
        cadena=""
        while(temp):
            cadena+=str(temp.item)+";"
            temp=temp.sig
        print(cadena)

    def borrar(self,kth):
        if(self.N>=kth):
            print("N>=kth",self.N,kth)
            if(kth>1):
                nodoAnt=self.cabeza
                for i in range(1,kth-1):
                    print(i,nodoAnt.item)
                    nodoAnt=nodoAnt.sig
                temp=nodoAnt.sig # lo copio
                print("temp:",temp.item)
                nodoAnt.sig=temp.sig
                if(nodoAnt.sig==None):
                    self.cola=nodoAnt
                self.N-=1
                return temp
            elif(kth==1):
                temp=self.eliminarCabeza()
                return temp
        else:
            return -1

    def buscar(self,key):
        temp=self.cabeza
        while(temp):
            if(str(temp.item)==str(key)):
                return True
            temp=temp.sig
        return False


q=listaEnlazada()
print(q.estaVacia())
q.agregar(1)
q.agregar(2)
q.agregar(3)
q.agregar(4)

# q.recorrer()
# q.eliminarCola()
# q.eliminarCabeza()
# q.recorrer()


# q.recorrer()
# print(q.borrar(1).item)
# print(q.borrar(1).item)
# q.recorrer()

q.recorrer()
print(q.buscar(7))
print(q.buscar(3))
print(q.buscar(4))
print(q.buscar(1))