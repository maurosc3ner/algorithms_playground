import numpy as np
import time
# Tiene dos metodos basicos
# el sort que es recursivo y llama por mitades
# y el merge que une los elementos al final 
#ctrl + shift+ p python select

class mergeSort:
    def sort(self,arr,low,high):

        # condicion de parada
        if (high>low):
            # encuentro la mitad del arreglo
            mid=low+int((high-low)/2)
            # ordeno la primera mitad
            self.sort(arr,low,mid)
            #ordeno la segunda mitad
            self.sort(arr,mid+1,high)
            self.merge(arr,low,mid,high)
    
    def merge(self,arr,low,mid,high):
        # print("debg:",arr,low,mid,high)
        N1=mid-low+1
        N2=high-mid
        left=np.zeros(N1)
        right=np.zeros(N2)
        #paso el arreglo a aux1 y 2
        i=0
        while(i<N1):
            left[i]=arr[low+i]
            i+=1
        i=0
        while(i<N2):
            right[i]=arr[mid+1+i]
            i+=1
        
        i=0
        j=0
        k=low
        # print("debg:",arr,i,j,k)
        while(i<N1 and j<N2):
            if(left[i]<right[j]):
                arr[k]=left[i]
                i+=1
            else:
                arr[k]=right[j]
                j+=1
            k+=1
        # desocupo el arr restante left
        while(i<N1):
            arr[k]=left[i]
            i+=1
            k+=1
        # desocupo el arr restante right
        while(j<N2):
            arr[k]=right[j]
            j+=1
            k+=1
        return arr
        # while(k<high):
        #     # si se acabo el vector izquiero, vacio el derecho 
        #     if(i>=mid):
        #         arr[k]=aux[j]
        #         j+=1
        #     # si se acabo el vector derecho, vacio el izquierdo
        #     elif(j>=high):
        #         arr[k]=aux[i]
        #         i+=1
        #     # el comparador
        #     elif(aux[i]<aux[j]):
        #         print("comp:",i,j)
        #         arr[k]=aux[i]
        #         i+=1
        #     else:
        #         arr[k]=aux[j]
        #         j+=1
        #     k+=1

N=10000
prg=mergeSort()
input=np.random.randint(0,100,N)
print(input)
start_time=time.time()
prg.sort(input,0,N-1)
print("mergeSort --- %s seconds ---" % (time.time() - start_time))
print(input)
# 1.5s N=100.000
# 19.5s N=1.000.000
# 206.6s N=10.000.000