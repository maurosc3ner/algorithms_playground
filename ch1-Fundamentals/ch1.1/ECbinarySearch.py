# Al igual que R se usa el # para comentar
# se usan los : en vez de ()
# no se usa los brackets {} para encerrar un codigo sino un tab
# no se usa ; para fin de linea
# python ECbinarySearch.py < ../tinyText.txt

import sys
import numpy as np

class miBusquedaBinaria:
    @staticmethod
    def buscador(llave, arr):
        inicio=0
        fin=len(arr)-1
        #version iterativa
        while(inicio<=fin):
            mitad=inicio+int((fin-inicio)/2)
            print ("Inicio {}, Fin {}, mitad {},arr {}".format(inicio,fin,mitad,arr[mitad]))
            if (llave<arr[mitad]): 
                fin=mitad-1
            elif (llave>arr[mitad]):
                inicio=mitad+1
            else:
                return mitad
        return -1
    
    def main(self):
        print("hello world!")
 

        # Using readlines() 
        file1 = open('../tinyAllowlist.txt', 'r') 
        Lines = file1.readlines() 
        count = 0
        # leida por ruta
        # Strips the newline character 
        permitidos=[]
        for line in Lines: 
            count =count+1
            print("Line{}: {}".format(count, line.strip())) 
            permitidos.append(int(line.strip()))
        
        sorted=np.sort(np.array(permitidos))
        # print (permitidos)
        print (np.sort(sorted))
        # leida por pipe 
        pipe=sys.stdin.readlines()
        print (pipe)
        for line in pipe:
            llave=int(line.strip())
            print(llave)
            if(self.buscador(llave,sorted) == -1):
                print("La llave {} no esta repetida".format(llave))


p1=miBusquedaBinaria()

p1.main()
