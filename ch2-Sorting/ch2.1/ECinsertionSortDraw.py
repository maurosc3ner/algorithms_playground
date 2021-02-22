
import numpy as np
import matplotlib.pyplot as plt
import random

random.seed(10)


class insertionSortDrawer:
    def __init__(self,N):
        super().__init__()
        self.N=N
    
    def exch(self,arr,a,b):
        swap=arr[a]
        arr[a]=arr[b]
        arr[b]=swap

    def sort(self,arr):
        # este sort no busca el min, cambia hacia atras
        fig, ax = plt.subplots()
        rects = ax.bar(range(self.N), arr)
        for i in range(0,N):
            for j in range(i,0,-1):
                if(arr[j]<arr[j-1]):
                    self.exch(arr,j,j-1)
                    for rect, h in zip(rects,arr):
                        rect.set_height(h) 
                        rect.set_color('b')
                    rects[i].set_color('r')
                    fig.canvas.draw()
                    plt.pause(0.01)
                else: break
        plt.show()
        return arr

N=50
prg=insertionSortDrawer(N)
input=np.random.randint(0,100,N)
print(input)

print(prg.sort(input))