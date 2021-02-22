
class nodo:
    def __init__(self,value):
        super().__init__()
        self.item=value
        self.sig=None

class colaLL:
    def __init__(self):
        super().__init__()
        self.cabeza=None
        self.cola=None
        self.N=0

    def tamano(self):
        return self.N
    
    def vacia(self):
        return (self.N==0)
    
    def encolar(self,value):
        
        nodoAnt=self.cola
        self.cola=nodo(value)
        if(self.vacia()):
            self.cabeza=self.cola
        else:
            nodoAnt.sig=self.cola
        self.N+=1

    def desencolar(self):
        if(self.cabeza!=None):
            self.cabeza=self.cabeza.sig
            self.N-=1
            if(self.vacia()):
                self.cola=None

    def atravesar(self):
        temp=self.cabeza
        micadena=""
        while(temp):
            micadena+=str(temp.item)+";"
            temp=temp.sig
        return micadena

prog=colaLL()
print(prog.vacia())
print(prog.tamano())
prog.encolar(1)
prog.encolar(2)
print(prog.vacia())
print(prog.tamano())
print(prog.atravesar())
prog.encolar(3)
prog.encolar(4)
print(prog.atravesar())
prog.desencolar()
print(prog.atravesar())