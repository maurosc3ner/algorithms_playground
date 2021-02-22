import numpy as np
import random
import time
import matplotlib.pyplot as plt
import math
# Este es un mergesort con calculo de accesos

class mergeSort:
    def __init__(self):
        super().__init__()
        self.access=0
    
    def sort(self,arr):
        if(len(arr)>1):
            mid=len(arr)//2
            # copia de las dos mitades
            lArr=arr[:mid]
            rArr=arr[mid:]
            self.access+=len(lArr)+len(rArr)
            #divide and conquer
            self.sort(lArr)
            self.sort(rArr)
            # sort
            i=j=k=0
            while(i<len(lArr) and j<len(rArr)):
                if(lArr[i]<rArr[j]):
                    arr[k]=lArr[i]
                    i+=1
                else:
                    arr[k]=rArr[j]
                    j+=1
                k+=1
                self.access+=1
            while(i<len(lArr)):
                arr[k]=lArr[i]
                i+=1
                k+=1
                self.access+=1
            while(j<len(rArr)):
                arr[k]=rArr[j]
                j+=1
                k+=1
                self.access+=1

N=100000
myalgo=list()
equ=list()
ave=list()
for n in range(1,N+1):
    prg=mergeSort()
    input=np.random.randint(0,1000,n)
    # print(len(input))
    # print(input)
    input=list(input.flatten())
    prg.sort(input)
    # print(np.array(input))
    myalgo.append(prg.access)
    equ.append(6*n*math.log(n))
    ave.append(n*math.log(n))
x=np.arange(1, N+1, 1)
print(len(myalgo),len(equ),x,len(x))

plt.figure()
plt.subplot()
plt.plot(x, np.array(myalgo), 'bo',label='mergesort')
plt.plot(x, np.array(equ), 'r--',label='upper bound (6N*Ln(N)')
plt.plot(x, np.array(ave), 'g--',label='avg bound (N*Ln(N)')
plt.title('mergesort accesses')
# Place a legend to the right of this smaller subplot.
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.5)
plt.show()