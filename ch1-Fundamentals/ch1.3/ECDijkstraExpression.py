

class evaluadorAritmetico:
    def __init__(self):
        super().__init__()
        #usa dos stacks (pilas) 
        self.operadores=list()
        self.valores=list()
    
    def evaluar(self,cadena):
        # el parentesis que abre se obvia
        # cada que haya un parentesis de cierre, significa un operacion mas pequena
        # se realiza esta operacion y se introduce el resultado en la ultima posicion
        for i in range(0,len(cadena)):
            if(cadena[i]=="("):
                print(i," abri (")
            elif(cadena[i]=="+"): 
                self.operadores.append("+")
            elif(cadena[i]=="-"):
                self.operadores.append("-")
            elif(cadena[i]=="*"):
                self.operadores.append("*")
            elif(cadena[i]=="/"):
                self.operadores.append("/")
            elif(cadena[i]==")"):
                op=self.operadores.pop()
                valorA=float(self.valores.pop())
                valorB=float(self.valores.pop())
                if (op=="+"):
                    self.valores.append(valorA+valorB)
                elif (op=="-"):
                    self.valores.append(valorA-valorB)
                elif (op=="*"):
                    self.valores.append(valorA*valorB)
                elif (op=="/"):
                    self.valores.append(valorA/valorB)
            else:
                self.valores.append(float(cadena[i]))
            print(self.valores)
            print(self.operadores)

        return self.valores.pop()

    def main(self):
        cadena="(1+((2+3)*(4*5)))"

        print(len(cadena),cadena)
        print(self.evaluar(cadena))
        


programa=evaluadorAritmetico()
programa.main()


