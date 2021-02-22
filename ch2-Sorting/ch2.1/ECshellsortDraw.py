import numpy as np
import matplotlib.pyplot as plt
import time

class shellSort:
    def __init__(self,N):
        super().__init__()
        self.N=N

    def exch(self,arr,a,b):
        swap=arr[a]
        arr[a]=arr[b]
        arr[b]=swap

    def sort(self,arr):
        hsort=1
        # generamos secuencia 3x+1
        while(hsort<self.N/3):
            hsort=3*hsort+1
            print(hsort)
        while(hsort>=1):
            for i in range(hsort,N):
                for j in range(i,0,-hsort):
                    if(arr[j]<arr[j-hsort]):
                        self.exch(arr,j,j-hsort)
            print(hsort)
            hsort=int(hsort/3)
        return arr
        
start_time=time.time()
N=1000000
prg=shellSort(N)
input=np.random.randint(0,100,N)
b=prg.sort(input)
print("shellsort --- %s seconds ---" % (time.time() - start_time))
print(b)
# 1461 seconds N=100000
