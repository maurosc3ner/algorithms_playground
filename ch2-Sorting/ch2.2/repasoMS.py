import numpy as np

class mergeSort:
    # no necesita indices
    def sort(self,arr):
        if len(arr)>1:
            mid=len(arr)//2
            # se parte en dos el arreglo
            le=arr[:mid]
            ri=arr[mid:]
            self.sort(le)
            self.sort(ri)
            # merge part
            self.merge(arr,le,ri)

    def merge(self,arr, le,ri):
        i=j=k=0
        while i<len(le) and j<len(ri):
            if le[i]<ri[j]:
                arr[k]=le[i]
                i+=1
            else:
                arr[k]=ri[j]
                j+=1
            k+=1
        while i<len(le):
            arr[k]=le[i]
            i+=1
            k+=1
        while j<len(ri):
            arr[k]=ri[j]
            j+=1
            k+=1

N=100
prg=mergeSort()
input=np.random.randint(0,1000,N)
print(len(input))
print(input)
input=list(input.flatten())
prg.sort(input)
print(np.array(input))

