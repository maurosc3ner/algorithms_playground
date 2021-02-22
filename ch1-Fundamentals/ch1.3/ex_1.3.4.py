# evaluador de corchetes en expresiones usando Stacks (pilas)
# la idea es la misma si esta bien construido una llave
# debe ser precedida por su cierre o por otra que vuelva y abra

class pilaLista:
    def __init__(self):
        super().__init__()
        self.pila=list()
        self.paren=0
        self.corch=0
        self.llav=0

    def tamano(self):
        return len(self.pila)
    
    def vacia(self):
        return (len(self.pila==0))

    def apilar(self,value):
        self.pila.append(value)
    
    def desapilar(self):
        return self.pila.pop()

    def evaluar(self,cadena):
        for i in range(0,len(cadena)):
            if(cadena[i]=="["):
                self.corch+=1
                self.apilar(cadena[i])
            elif(cadena[i]=="("):
                self.paren+=1
                self.apilar(cadena[i])
            elif(cadena[i]=="{"):
                self.llav+=1
                self.apilar(cadena[i])
            elif(cadena[i]=="]"):
                item=self.desapilar()
                if (item!="["):
                    return False
                self.corch-=1
            elif(cadena[i]==")"):
                item=self.desapilar()
                print("desapilo:",item)
                if (item!="("):
                    return False
                self.paren-=1
            elif(cadena[i]=="}"):
                item=self.desapilar()
                if (item!="{"):
                    return False
                self.llav-=1
            print(cadena[i],"  :  ",self.pila)
        print("resumen parentesis:{}; corchetes:{}; llaves{}".format(self.paren,self.corch,self.llav))
        return True






prog=pilaLista()

cadena="[()]{[()()]()}"

print(prog.evaluar(cadena))

print(prog.evaluar("[(])"))


