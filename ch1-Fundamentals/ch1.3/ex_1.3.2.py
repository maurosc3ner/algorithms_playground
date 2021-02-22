

class pila:
    def __init__(self):
        super().__init__()
        self.pila=list()

    def tamano(self):
        return len(self.pila)

    def vacia(self):
        return (len(self.pila)==0)

    def apilar(self,valor):
        self.pila.append(valor)
    
    def desapilar(self):
        return self.pila.pop()

    def __iter__(self):
        return iter(self.pila)

"it-was-the-best-of-times---it-was-the--"
prog=pila()
prog.apilar("it")
prog.apilar("-")
prog.apilar("was")
prog.apilar("-")
prog.apilar("the")
prog.apilar("-")
prog.apilar("best")
prog.apilar("-")
prog.apilar("of")
prog.apilar("-")
prog.apilar("times")
prog.apilar("---")
prog.apilar("it")
prog.apilar("-")
prog.apilar("was")
prog.apilar("-")
prog.apilar("the")
prog.apilar("--")
print(prog.pila)