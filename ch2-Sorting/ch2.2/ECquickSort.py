import numpy as np
import random
import time
import matplotlib.pyplot as plt
import math
import sys
print(sys.getrecursionlimit())  # limite de llamadas recursivas de python
sys.setrecursionlimit(15000000)

class quickSort:
    def sort1(self,arr):
        random.shuffle(arr) # QS no es estable, este shuffle ayuda a que lo sea probabilisticamente
        print("barajamiento hecho")
        self.sort(arr,0,len(arr)-1)

    def sort(self,arr,start,end):
        if(start<end):
            pvt=self.partition2(arr,start,end)
            # self.sort(arr,start,pvt-1)
            self.sort(arr,start,pvt)
            self.sort(arr,pvt+1,end)

    def exch(self,arr,a,b):
        swap=arr[a]
        arr[a]=arr[b]
        arr[b]=swap
    
    # particion basado de mycodeschool youtube
    def partition(self,arr,start, end):
        pivot=arr[end]
        pidx=start
        # str1
        # arr[end],arr[start+(end-start)//2] = arr[start+(end-start)//2],arr[end] #change to fix worst case for the pivot selection
        for i in range(start,end):
            if(arr[i]<pivot):
                self.exch(arr,i,pidx)
                pidx+=1 
        self.exch(arr,pidx,end)
        return pidx
    
    # partition mejorado tomado de:
    # https://stackabuse.com/sorting-algorithms-in-python/#heapsort
    def partition2(self,arr,start, end):
        pivot=arr[(start+end)//2]
        i = start - 1
        j = end + 1
        while True:
            i += 1
            while arr[i] < pivot:
                i += 1
            j -= 1
            while arr[j] > pivot:
                j -= 1
            if i >= j:
                return j
            # If an element at i (on the left of the pivot) is larger than the
            # element at j (on right right of the pivot), then swap them
            self.exch(arr,i,j)
        
n=8
prg=quickSort()
input=np.random.randint(0,100,n)
# print(len(input))
print(input)
input=list(input.flatten())
start_time=time.time()
prg.sort1(input)
print("quickSort --- %s seconds ---" % (time.time() - start_time))
print(np.array(input))
# 0.78s N=100.000   
# 33.1s N=1.000.000   
# 73.4s N=10.000.000 
# 956.7s N=100.000.000