import matplotlib.pyplot as plt
import numpy as np

class shellSortDraw:
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
        # fig, ax = plt.subplots()
        # rects = ax.bar(range(self.N), arr)
        while(hsort>=1):
            i=hsort
            while(i<self.N):
                j=i
                while(j>0 and arr[j]<arr[j-hsort]):
                    self.exch(arr,j,j-hsort)
                    # for rect, h in zip(rects,arr):
                    #     rect.set_height(h) 
                    #     rect.set_color('b')
                    # rects[i].set_color('r')
                    # fig.canvas.draw()
                    # plt.pause(0.05)
                    j-=hsort
                
                i+=1

            hsort=int(hsort/3)
        plt.show()
        return arr

N=10000
prg=shellSortDraw(N)
input=np.random.randint(0,100,N)
print(input)

print(prg.sort(input))