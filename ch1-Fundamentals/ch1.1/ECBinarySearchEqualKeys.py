import sys
import numpy as np

class ex_1_1_29:

    def buscar(self, llave, arr):
        inicio=0
        fin=len(arr)-1
        encontrados=0
        menores=0
        while(inicio<=fin):
            mitad=inicio+int((fin-inicio)/2)
            print ("Inicio {}, Fin {}, mitad {},arr {}, menores {}".format(inicio,fin,mitad,arr[mitad],menores))

            if (llave<arr[mitad]):
                fin=mitad-1
            elif (llave>arr[mitad]):
                # menores=menores+mitad-inicio
                inicio=mitad+1
            else:
                menores=mitad
                encontrados+=1
                arr=np.delete(arr,mitad)
                
                # return mitad

        if( encontrados>0):
            print("La llave {} fue encontrada {} veces y {} elementos son menores a ella {}".format(llave,encontrados, menores, mitad))
            return [menores,encontrados]
        else:
            print("no encontrada")

    def main(self):
        # cargo el archivo fisico
        # ruta, permisos
        file1=open("../TinyAllowlist2.txt","r")
        lineas1=file1.readlines()

        temp1=[]
        for linea1 in lineas1:
            temp1.append(int(linea1))

        ordenado=np.sort(temp1)
        print(temp1, ordenado)
        rank,count=self.buscar(12,ordenado)
        print(ordenado[rank:rank+count])
        rank,count=(self.buscar(77,ordenado))
        print(ordenado[rank:rank+count])
        rank,count=self.buscar(33,ordenado)
        print(ordenado[rank:rank+count])

programa=ex_1_1_29()
programa.main()