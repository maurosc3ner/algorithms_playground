import numpy as np


class selectionSort:
    def __init__(self,N):
        super().__init__()
        self.arr=np.zeros(N,dtype=int)
        self.N=N
    def exch(self,a,b):
        swap=self.arr[a]
        self.arr[a]=self.arr[b]
        self.arr[b]=swap
    def sort(self):
        for i in range(0,self.N):
            # suponemos que arr[i] es el minimo antes de irlo a comparar
            minIdx=i
            # hayar el min
            for j in range(i+1,self.N):
                if (self.arr[j]<self.arr[minIdx]): minIdx=j
            self.exch(i,minIdx)

    

N=10
prg=selectionSort(N)
input=np.random.randint(0,100,N)
print(input)
for i in range(0,N):
    prg.arr[i]=int(input[i])

prg.sort()

print(prg.arr)
