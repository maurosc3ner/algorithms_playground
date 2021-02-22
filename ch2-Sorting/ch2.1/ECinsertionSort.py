import numpy as np
# import matplotlib.pyplot as plt
import time
import sys

class insertionSort:
    def __init__(self,N):
        # super().__init__()
        self.arr=np.zeros(N,dtype=int)
        self.N=N
    def exch(self,a,b):
        swap=self.arr[a]
        self.arr[a]=self.arr[b]
        self.arr[b]=swap
    def sort(self):
        for i in range(0,self.N):
            for j in range(i,0,-1):
                if(self.arr[j]<self.arr[j-1]):
                    self.exch(j-1,j)
                else: break
N=int(sys.argv[1])
prg=insertionSort(N)
input=np.random.randint(0,100,N)

print(input)
for i in range(0,N):
    prg.arr[i]=int(input[i])
start_time=time.time()
prg.sort()
print(prg.arr)
print("insertsort --- %s seconds ---" % (time.time() - start_time))
# 2013 seconds N=100000