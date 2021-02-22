import numpy as np
import random
import time
import matplotlib.pyplot as plt
#esta es una version simplificada basada en geeks for code y el libro
# es mas legible y entendible

class mergeSort:
    def sort(self,arr):
        if(len(arr)>1):
            mid=len(arr)//2 # operador // toma solo la parte entera
            leftArr=arr[:mid]
            rightArr=arr[mid:]
            self.sort(leftArr)
            self.sort(rightArr)
            
            i=0
            j=0
            k=0  # para el arreglo final
            while (i<len(leftArr) and j<len(rightArr)):
                if(leftArr[i]<rightArr[j]):
                    arr[k]=leftArr[i]
                    i+=1
                else:
                    arr[k]=rightArr[j]
                    j+=1
                k+=1
            # print("ijk:",i,j,k)
            while(i<len(leftArr)):
                arr[k]=leftArr[i]
                i+=1
                k+=1
            while(j<len(rightArr)):
                arr[k]=rightArr[j]
                j+=1
                k+=1
N=10000
prg=mergeSort()
input=np.random.randint(0,1000,N)
print(len(input))
print(input)
input=list(input.flatten())
start_time=time.time()
prg.sort(input)
print("mergeSort --- %s seconds ---" % (time.time() - start_time))
print(np.array(input))
# 0.58s N=100.000   
# 6.5s N=1.000.000   
# 90.0s N=10.000.000 
# 1090.9s N=100.000.000