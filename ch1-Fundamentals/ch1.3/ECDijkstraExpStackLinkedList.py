

class nodo:
    def __init__(self,item):
        super().__init__()
        self.item=item
        self.sig=None

class StackDijkstra:
    def __init__(self):
        super().__init__()
        self.cabeza=None
        self.cola=None
    
    # ni tamano N, ni vacio es necesario
    def push(self,item):
        nodoAnt=self.cabeza
        self.cabeza=nodo(item)
        self.cabeza.sig=nodoAnt
        if(nodoAnt==None):
            self.cola=self.cabeza

    def pop(self):
        item=self.cabeza.item
        self.cabeza=self.cabeza.sig
        if(self.cabeza==None):
            self.cola=None
        return item

cadena="(1+((2+3)*(4*5)))"
print(len(cadena),cadena)
operadores=StackDijkstra()
valores=StackDijkstra()

for i in range(0,len(cadena)):
    if(cadena[i]=="("):
        print("abre (")
    elif(cadena[i]=="+" or cadena[i]=="-" or cadena[i]=="*" or cadena[i]=="/"):
        operadores.push(cadena[i])
    elif(cadena[i]==")"):
        op=operadores.pop()
        A=float(valores.pop())
        B=float(valores.pop())
        if(op=="+"):
            valores.push(str(A+B))
        elif(op=="-"):
            valores.push(str(A-B))
        elif(op=="*"):
            valores.push(str(A*B))
        elif(op=="/"):
            valores.push(str(A/B))
    else:
        valores.push(cadena[i])
print(valores.pop())

