
def peso(op):
    switcher ={
        "+":1,
        "-":1,
        "*":2,
        "/":2
    }
    return switcher.get(op)

def precedencia(w1,w2):

    if w1>=w2:
        return True
    else:
        return False


def infix2Postfix(exp):
    op=pilaLista()
    out=pilaLista()
    for i in range(0,len(exp)):
        # print(out.mipila)
        # print(op.mipila)
        if(exp[i] in "0123456789" or exp[i] in "ABCDEFGHIJKLMNOPQRSTUXYZ"):
            out.apilar(exp[i])
        elif(exp[i] in "+-/*"):
            print("operador",exp[i],op.ultimo())
            while(not(op.estaVacia()) and op.ultimo()!="(" and precedencia(peso(op.ultimo()),peso(exp[i]))):
                    out.apilar(op.desapilar())
            
            op.apilar(str(exp[i]))
        elif(exp[i]=="("):
            op.apilar(exp[i])
        elif(exp[i]==")"):    
            while(not(op.estaVacia()) and op.ultimo()!="("):
                out.apilar(op.desapilar())
            op.desapilar()

    while(not(op.estaVacia())):
        out.apilar(op.desapilar())

    return out


# def evaluar(pila):
#     values=pilaLista()
#     op2=pilaLista()
#     for item in pila:
#         if (item in "0123456789"):
#             values.apilar(item)
#         elif(item=="+"):



class pilaLista:
    def __init__(self):
        super().__init__()
        self.mipila=list()
    
    def tamano(self):
        return len(self.mipila)
    
    def estaVacia(self):
        return (len(self.mipila)==0)
    
    def apilar(self,value):
        self.mipila.append(value)
    
    def desapilar(self):
        if(not self.estaVacia()):
            return self.mipila.pop()

    def __iter__(self):
        return iter(self.mipila)
    #peek
    def ultimo(self):
        if(not self.estaVacia()):
            return self.mipila[self.tamano()-1]



print(infix2Postfix("A+B*C").mipila)

print(infix2Postfix("X+Y*Z-T*U").mipila)

print(infix2Postfix("((A+B)*C-D)*E").mipila)

print(infix2Postfix("1+2*3-4*5").mipila)
