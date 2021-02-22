# Knuth Shuffle es un barajamiento en tiempo lineal vs el tipico
# que seria generar un vector aleatorio float, asignarlo a cada elemento
# y luego ordenar ese vector float que si fuese QS podria ser minimo O(NLnN)
import random
import numpy as np
class knuthSuffle:
    def exch(self,arr,a,b):
        swap=arr[a]
        arr[a]=arr[b]
        arr[b]=swap

    def shuffler(self,arr):
        for i in range (0, len(arr)):
            r=random.randint(0,i)
            print(i, r)
            self.exch(arr,i,r)
        return arr


n=10
input=np.random.randint(0,100,n)
input.sort()

print(input)

prg=knuthSuffle()
b=prg.shuffler(list(input.flatten()))
print(b)