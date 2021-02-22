import numpy as np
import random
import time
import matplotlib.pyplot as plt
import math
import sys
print(sys.getrecursionlimit())  # limite de llamadas recursivas de python
sys.setrecursionlimit(15000000)


class qsBook:
    def exch(self,arr,a,b):
        swap=arr[a]
        arr[a]=arr[b]
        arr[b]=swap
    def sort1(self,arr):
        random.shuffle(arr)
        self.sort(arr,0,len(arr)-1)
    def sort(self,arr,start,end):
        if(start<end):
            pvt=self.partition(arr,start,end)
            self.sort(arr,start,pvt-1)
            self.sort(arr,pvt+1,end)
    def partition(self,arr,start,end):
        # pidx=(start+end)//2 # descartado tunning de punto medio
        pivot=arr[start]
        i=start
        j=end+1
        while True:
            i+=1
            while arr[i]<pivot: # arr[++i] se llama pre-increment
                if(i==j): break
                i+=1
            j-=1
            while arr[j]>pivot: # arr[++i] se llama pre-increment
                if(i==j): break
                j-=1 
            if(i>=j): break
            self.exch(arr,i,j)
        self.exch(arr,start,j)
        return j

n=8
prg=qsBook()
input=np.random.randint(0,1000,n)
# print(len(input))
print(input)
input=list(input.flatten())
start_time=time.time()
prg.sort1(input)
print("quickSort --- %s seconds ---" % (time.time() - start_time))
print(np.array(input))
# no funciona bien