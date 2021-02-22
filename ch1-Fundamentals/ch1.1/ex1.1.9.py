# conversor binario int

class ex_1_1_9:
    def main(self):
        N=int(input('Entero:'))

        cosciente=N
        residuo=0
        binario=''
        while(cosciente>0):
            residuo=cosciente%2
            cosciente=int(cosciente/2)
            
            binario=str(residuo)+binario
            print(cosciente)
        
        print(binario)

programa=ex_1_1_9()
programa.main()