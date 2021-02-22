import sys
import numpy as np
class ex_1_1_28:

    def busqueda(self,llave,arr):
        inicio=0
        fin=len(arr)-1
        #version iterativa
        while(inicio<=fin):
            mitad=inicio+int((fin-inicio)/2)
            print ("Inicio {}, Fin {}, mitad {},arr {}".format(inicio,fin,mitad,arr))
            # cuidado con los if
            if(llave<arr[mitad]): 
                fin=mitad-1
            elif(llave>arr[mitad]): 
                inicio=mitad+1
            else: 
                return mitad
        return -1
    def miCleaner(self,arr):
        j=0
        # largo del vector len(arr)
        while j<len(arr)-1:
            last=arr[j]
            i=j+1
            while i<len(arr):
                if last==arr[i]:
                    print("antes:",arr)
                    arr=np.delete(arr,i)
                    print("elemento repetido:",arr)
                else: i+=1    
            j+=1
        return arr

    def main (self):
        # open abre un archivo
        file1=open("../tinyAllowlist2.txt","r")
        # separa el archivo linea por linea en una lista de objetos tipo caracter
        lines1=file1.readlines()
        # lo pasamos a un arreglo casteados
        permitidos=[]
        for i in lines1:
            #  strip() borra los espacios en blanco y newline
            permitidos.append(int(i))

        print(lines1)
        print(permitidos)
        sorted=np.sort(permitidos)
        print(sorted,type(sorted))
        limpio=self.miCleaner(sorted)
        print(limpio)

        pipe=sys.stdin.readlines()
        for lines2 in pipe:
            llave=int(lines2.strip())
            print(llave)
            if(self.busqueda(llave,limpio)==-1):
                print("llave:" ,llave," no encontrada en:",limpio)



programa=ex_1_1_28()
programa.main()

