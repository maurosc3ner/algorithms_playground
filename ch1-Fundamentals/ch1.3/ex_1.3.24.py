

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
    def agregar(self,value):
        nodoAnt=self.cola
        self.cola=nodo(value)
        if not(self.estaVacia()):
            nodoAnt.sig=self.cola
        else:
            self.cabeza=self.cola
        # aumento al final
        self.N+=1
    def eliminarCabeza(self):
        if not(self.estaVacia()):
            nodoAnt=self.cabeza
            self.cabeza=self.cabeza.sig
            self.N-=1
            # si tenia un solo elemento, debo avisarle a la cola
            # que quedo en None
            if self.estaVacia():
                self.cola=None
            return nodoAnt
    def eliminarCola(self):
        if(self.N>1):
            temp=self.cabeza
            #toca recorrer la lista hasta el penultimo elemento
            while(temp.sig.sig):
                temp=temp.sig
            # luego de que he ido hasta el penultimo y esta en temp
            nodoAnt=self.cola
            self.cola=temp
            self.cola.sig=None
        elif self.N==1:
            nodoAnt=self.cola
            self.cola=None
            self.cabeza=None
        else: 
            return -1 
        self.N-=1
        return nodoAnt
    def recorrer(self):
        temp=self.cabeza
        cadena=""
        while(temp):
            cadena+=str(temp.item)+";"
            temp=temp.sig
        print(cadena)
    def borrarKth(self,kth):
        #garantizar que N elementos>=kth elemento buscado
        if self.N>=kth:
            #hay dos casos kth>1 
            if kth>1:
                temp=self.cabeza
                #hay que iterar hasta el kth elemento anterior
                for i in range(1,kth-1):
                    temp=temp.sig
                nodoAnt=temp.sig
                temp.sig=nodoAnt.sig
                # si kth era el ultimo actualizo la cola
                if(temp.sig==None):
                    self.cola=temp
                self.N-=1
                return nodoAnt
            # kth==1
            elif kth==1:
                return self.eliminarCabeza()
            else:
                return -1
    # ex1.3.24
    def borrarDespues(self,value):
        temp=self.cabeza
        idx=1
        while(temp):
            if temp.item==value:
                self.borrarKth(idx+1)
            idx+=1
            temp=temp.sig
    def buscar(self,key):
        temp=self.cabeza
        idx=1
        while(temp):
            if(str(temp.item)==str(key)):
                return { 'estaPresente': True, 'idx':idx, 'nodoAnt':temp}
            idx+=1
            temp=temp.sig
        return { 'estaPresente': False, 'idx':-1, 'nodoAnt':None}
    # ex1.3.26 
    def borrador(self,key):
        # reusamos buscar
        busqueda=self.buscar(key)
        print(busqueda,busqueda['estaPresente'])
        while(busqueda['estaPresente']):
            self.borrarKth(busqueda['idx'])
            # reusamos buscar luego de haber eliminado el kth
            busqueda=self.buscar(key)
            print(busqueda,busqueda['estaPresente'])
    # ex 1.3.25
    def insertarDespues(self,key,item):
        busqueda=self.buscar(key)
        if(busqueda['estaPresente']):
            if(busqueda['nodoAnt'].sig!=None):
                temp=nodo(item)
                temp.sig=busqueda['nodoAnt'].sig
                busqueda['nodoAnt'].sig=temp
            #si solo hay un elemento se reusa agregar
            else:
                self.agregar(item)
    # ex 1.3.27
    def max(self):
        temp=self.cabeza
        max=0
        if self.estaVacia():
            print(max)
        else:
            while(temp):
                if(temp.item>max):
                    max=temp.item
                temp=temp.sig
            print(max)
    def maxRecur(self,nodoTemp,currentMax):
        if nodoTemp==None:
            print(currentMax)
            return -1
        if nodoTemp.item>currentMax:
            currentMax=nodoTemp.item
        return self.maxRecur(nodoTemp.sig,currentMax)

#probar 1.3.20
# q=listaEnlazada()
# print(q.estaVacia())
# q.agregar(1)
# q.agregar(2)
# q.agregar(3)
# # q.agregar(4)
# q.recorrer()
# q.borrarKth(2)
# q.recorrer()

# probar 1.3.24
# q=listaEnlazada()
# print(q.estaVacia())
# q.agregar(1)
# q.agregar(2)
# q.agregar(3)
# q.recorrer()
# q.borrarDespues(2)
# q.recorrer()

# probar 1.3.25
# q=listaEnlazada()
# print(q.estaVacia())
# q.agregar(1)
# # q.agregar(2)
# # q.agregar(4)
# q.recorrer()
# # q.insertarDespues(2,3)
# q.insertarDespues(1,3)
# q.recorrer()

# probar 1.3.26
# q=listaEnlazada()
# print(q.estaVacia())
# q.agregar(2)
# q.agregar(2)
# q.agregar(3)
# q.recorrer()
# q.borrador(2)
# q.recorrer()

# probar 1.3.27
# q=listaEnlazada()
# print(q.estaVacia())
# q.agregar(2)
# q.agregar(7)
# q.agregar(3)
# q.recorrer()
# q.max()

# probar 1.3.28
q=listaEnlazada()
q.agregar(10)
q.agregar(2)
q.agregar(3)
q.recorrer()
q.max()
q.maxRecur(q.cabeza,0)