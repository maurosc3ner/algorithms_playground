import time
import numpy as np
import matplotlib.pyplot as plt
import math

class UF_weightQU:
    def __init__(self,N):
        super().__init__()
        self.id=np.arange(N)
        self.size=np.zeros(N)
        self.acce=0
        self.N=N
        self.comp=N
        print("inicializado:",self.N,self.comp)

    def find(self,i):
        while(i!=self.id[i]):
            self.acce+=1
            i=self.id[i]
        return i

    def weightedQU(self,p,q):
        pID=self.find(p)
        qID=self.find(q)
        if(pID==qID): return -1

        if(self.size[pID]<self.size[qID]):
            self.id[pID]=qID
            self.size[qID]+=self.size[pID]
        else:
            self.id[qID]=pID
            self.size[pID]+=self.size[qID]
        self.acce+=1    
        self.comp-=1


start_time=time.time()
file1=open("tinyUF_1.5.1.txt","r")
lines=file1.readlines()
N=int(lines.pop(0))
prg=UF_weightQU(N)
for line in lines:
    pq=line.split()
    prg.weightedQU(int(pq[0]),int(pq[1]))
B=np.reshape(prg.id,(int(5),-1))
print("weighted quickunion --- %s seconds ---" % (time.time() - start_time),prg.N,prg.acce,prg.comp,prg.id)
plt.imshow(B)
plt.show()


start_time=time.time()
file1=open("mediumUF.txt","r")
lines=file1.readlines()
N=int(lines.pop(0))
prg=UF_weightQU(N)
for line in lines:
    pq=line.split()
    prg.weightedQU(int(pq[0]),int(pq[1]))
B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
print("weighted quickunion --- %s seconds ---" % (time.time() - start_time),prg.N,prg.acce,prg.comp)
plt.imshow(B)
plt.show()

start_time=time.time()
file1=open("largeUF.txt","r")
lines=file1.readlines()
N=int(lines.pop(0))
prg=UF_weightQU(N)
for line in lines:
    pq=line.split()
    prg.weightedQU(int(pq[0]),int(pq[1]))
B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
print("weighted quickunion --- %s seconds ---" % (time.time() - start_time),prg.N,prg.acce,prg.comp)
plt.imshow(B)
plt.show()