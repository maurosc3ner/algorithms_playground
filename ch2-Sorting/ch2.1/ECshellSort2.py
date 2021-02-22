import sys
import time
import numpy as np

class shellSort2:
    def __init__(self,N):
        super().__init__()
        self.N=N

    def exch(self,arr,a,b):
        swap=arr[a]
        arr[a]=arr[b]
        arr[b]=swap
    def sort(self,arr):
        hsort=1
        while(hsort<self.N/3):hsort=3*hsort+1
        while(hsort>=1):
            i=hsort
            while(i<self.N):
                j=i
                while(j>0 and (arr[j]<arr[j-hsort])):
                    self.exch(arr,j,j-hsort)
                    j-=hsort
                i+=1
            print(hsort)
            hsort=int(hsort/3)
        return arr
    def check(self,arr):
        i=1
        flag=True
        while (i<self.N):
            if(arr[i-1]>arr[i]):
                flag=False
                break
            i+=1
        return flag

N=int(sys.argv[1])
prg=shellSort2(N)
input=np.random.randint(0,100,N)
# print(input)
print(prg.check(input))
start_time=time.time()
b=prg.sort(input)
print("shellsort2 --- %s seconds ---" % (time.time() - start_time))
# print(b)
print(prg.check(b))
#~3s N=100.000
#28.3s N=1.000.000
#308.4s N=10.000.000