# version 2 mejorada
import sys
import time
import numpy as np

class insertionSort2:
    def __init__(self,N):
        self.N=N
    def exch(self,arr,a,b):
        swap=arr[a]
        arr[a]=arr[b]
        arr[b]=swap
    def sort(self,arr):\
        # arranca en 1 por el arr[j-1]
        i=1
        while(i<self.N):
            j=i
            while(j>0 and (arr[j]<arr[j-1])):
                self.exch(arr,j,j-1)
                # ciclo interno va hacia atras j>0
                j-=1
            i+=1
        return arr


N=int(sys.argv[1])
prg=insertionSort2(N)
input=np.random.randint(0,100,N)
print(input)
start_time=time.time()
b=prg.sort(input)
print("insertionsort2 --- %s seconds ---" % (time.time() - start_time))
print(b)
# 16.5s N=10.000
# 1705s N=100.000

