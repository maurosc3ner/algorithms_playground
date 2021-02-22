import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(10)

class selectionSort:
    def __init__(self,N):
        super().__init__()
        self.N=N

    def exch(self,arr,a,b):
        swap=arr[a]
        arr[a]=arr[b]
        arr[b]=swap
    
    def sort(self,arr):
        fig, ax = plt.subplots()
        rects = ax.bar(range(self.N), arr)
        for i in range(0,N):
            min=i
            for j in range(i,N):
                if(arr[j]<arr[min]): 
                    min=j
            self.exch(arr,i,min)
            for rect,h in zip(rects,arr):
                rect.set_height(h) 
                # ax.text(rect.get_x() + rect.get_width()/2.,1.05*h,'%d' % int(h),ha='center', va='bottom')

            fig.canvas.draw()
            plt.pause(0.3)
        plt.show()
        return arr

N=100
prg=selectionSort(N)
input=np.random.randint(0,100,N)
print(input)

print(prg.sort(input))

