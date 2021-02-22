# Al igual que R se usa el # para comentar
# se usan los : en vez de ()
# no se usa los brackets {} para encerrar un codigo sino un tab
# no se usa ; para fin de linea
# python ECbinarySearchRecursiva.py < ../tinyText.txt -

# incluye ejercicios 1.1.22 y 1.1.23

import sys
import numpy as np

class miBusquedaBinaria:
    # version recursiva   
    def buscadorR(self,llave, inicio, fin, arr,depth,imprimir):
        mitad=inicio+int(fin-inicio)/2
        current="Llave {},Inicio {}, Fin {}, mitad {},arr[mitad] {}".format(llave,inicio,fin,mitad,arr[mitad])
        print (" "*depth+current)
        depth=depth+1
        if inicio>fin:
            if imprimir=='+': 
                print("No esta repetido="+str(llave))
            return -1
        if llave<arr[mitad]: 
            self.buscadorR(llave,inicio,mitad-1,arr,depth,imprimir)
        elif llave>arr[mitad]:
            self.buscadorR(llave,mitad+1,fin,arr,depth,imprimir)
        else: 
            if imprimir=='-': 
                output="Encontrado en arr["+str(mitad)+"]="+str(arr[mitad])
                print(output)
            return mitad
    
    def main(self):
       
        # Using readlines() 
        file1 = open('../tinyAllowlist.txt', 'r') 
        Lines = file1.readlines() 
        count = 0
        # leida por ruta
        # Strips the newline character 
        permitidos=[]
        for line in Lines: 
            count =count+1
            # print("Line{}: {}".format(count, line.strip())) 
            permitidos.append(int(line.strip()))
        
        sorted=np.sort(np.array(permitidos))
        # print (permitidos)
        print (np.sort(sorted))
        # leida por pipe 
        pipe=sys.stdin.readlines()
        print (pipe)
        print ('Argument List:', str(sys.argv))
        for line in pipe:
            llave=int(line.strip())
            print(llave)
            inicio=0
            fin=len(sorted)-1
            self.buscadorR(llave,inicio,fin,sorted,0,sys.argv[1])


p1=miBusquedaBinaria()

p1.main()
