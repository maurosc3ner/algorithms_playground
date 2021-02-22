import random
import numpy as np
import sys
print(sys.getrecursionlimit())  # limite de llamadas recursivas de python
sys.setrecursionlimit(15000)
class repasoQS:
    def __init__(self,N):
        super().__init__()
        input=np.random.randint(0,1000,N)
        # print(len(input))
        print(input)
        self.arr=list(input.flatten())

    def sort1(self):
        random.shuffle(self.arr)
        # print(self.arr)
        self.sort(0,len(self.arr)-1)

    def exch(self,a,b):
        swap=self.arr[a]
        self.arr[a]=self.arr[b]
        self.arr[b]=swap

    def sort(self,start,end):
        # print("optimized quickSort mode")
        if((end-start)<=20):
            self.insertionSort(start,end)
        if start<end:
            pvt=self.partition(start,end)
            self.sort(start,pvt)
            self.sort(pvt+1,end)

    def partition(self,start,end):
        pivot=self.arr[(start+end)//2]
        i=start-1
        j=end+1

        while True:
            i+=1
            # es mayor que el pivote? sino no hay necesidad de mover 
            # aumento indice
            while self.arr[i]<pivot: 
                i+=1
            j-=1
            # es menor que el pivote? sino no hay necesidad de mover 
            # disminuyo indice j
            while self.arr[j]>pivot:
                j-=1
            if i>=j: return j
            self.exch(i,j)

    def insertionSort(self,start,end):
        # print("cutoff (insertionSort) mode")
        i=start+1
        while i<end:
            j=i
            while j>start and self.arr[j]<self.arr[j-1]:
                self.exch(j,j-1)
                j-=1
            i+=1

prg=repasoQS(10000)
prg.sort1()
print(prg.arr)