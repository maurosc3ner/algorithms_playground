import random
import numpy as np
import matplotlib.pyplot as plt
import time

class qsCutDraw:
    def __init__(self):
        super().__init__()
        self.arr=[]
        self.fig, self.ax = plt.subplots()
        self.rects = []

        # 
    
    def exch(self,a,b):
        swap=self.arr[a]
        self.arr[a]=self.arr[b]
        self.arr[b]=swap

    def sort1(self):
        random.shuffle(self.arr)
        self.sort(0,len(self.arr)-1)

    def insertionSort(self,start,end):
        print("cutoff (insertionSort) mode")
        i=start+1
        while i<end:
            j=i
            while (j>0 and self.arr[j]<self.arr[j-1]):
                self.exch(j,j-1)
                j-=1
            i+=1

    def sort(self,start,end):
        print("optimized quickSort mode")
        if(end-start<30):
            self.insertionSort(start,end)
        if(start<end):
            pvt=self.partition(start,end)
            self.sort(start,pvt)
            self.sort(pvt+1,end)

    def partition(self,start,end):
        pivot=self.arr[(start+end)//2]
        i=start-1
        j=end+1

        while True:
            i+=1
            while (self.arr[i]<pivot):
                i+=1
            j-=1
            while (self.arr[j]>pivot):
                j-=1

            if(i>=j): return j
            self.exch(i,j)
            for rect, h in zip(self.rects,self.arr):
                rect.set_height(h) 
                rect.set_color('b')
            self.rects[i].set_color('r')
            self.rects[j].set_color('r')
            self.fig.canvas.draw()
            plt.pause(0.01)
        plt.show()

    def main(self,n):
        input=np.random.randint(0,100,n)
        # print(len(input))
        print(input)
        self.arr=list(input.flatten())
        self.rects=self.ax.bar(range(n), self.arr)
        # start_time=time.time()
        self.sort1()
        
        # print("quickSort --- %s seconds ---" % (time.time() - start_time))
        

n=250
prg=qsCutDraw()
prg.main(n)
print(np.array(prg.arr))
