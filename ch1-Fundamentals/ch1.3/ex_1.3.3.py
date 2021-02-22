
class pilaLista:
    def __init__(self):
        super().__init__()
        self.pila=list()

    def tamano(self):
        return len(self.pila)

    def vacia(self):
        return (len(self.pila==0))
    
    def apilar(self,value):
        self.pila.append(int(value))
    
    def desapilar(self):
        self.pila.pop()

prog=pilaLista()
prog.apilar(0)
