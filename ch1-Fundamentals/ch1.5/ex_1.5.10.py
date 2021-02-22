import time
import math
import matplotlib.pyplot as plt
import numpy as np

class UF_weightedQU_mod:
    def __init__(self,N):
        super().__init__()
        self.id=np.arange(N)
        self.size=np.zeros(N)
        self.comp=N
        self.N=N
        print("inicializado:",self.N,self.comp)
    
    def find(self,i):
        while(i!=self.id[int(i)]): i=self.id[int(i)]
        return i
    
    def weightedQUmod1(self,p,q):
        pID=self.find(p)
        qID=self.find(q)
        #si son iguales es porque estan en el mismo componente
        if(pID==qID):
            return -1
        if(self.size[pID]<self.size[qID]):
            # 1.5.10 mod
            self.id[pID]=q
            self.size[qID]+=self.size[pID]
        else:
            # 1.5.10 mod
            self.size[pID]+=p
            self.size[pID]+=self.size[qID]
        self.comp-=1
        
    def weightedQUmod2(self,p,q):
        pID=self.find(p)
        qID=self.find(q)
        # si son iguales es porque estan en el mismo componente
        if(pID==qID):
            return -1
        if(self.size[pID]<self.size[qID]):
            self.id[pID]=self.id[qID]
            self.size[pID]+=self.size[qID]
        else:
            self.id[qID]=self.id[pID]
            self.size[qID]=self.size[pID]
        self.comp-=1


start_time=time.time()
file1=open("mediumUF.txt","r")
lines=file1.readlines()
N=int(lines.pop(0))
prg=UF_weightedQU_mod(N)
for line in lines:
    pq=line.split()
    prg.weightedQUmod1(int(pq[0]),int(pq[1]))
B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
print("weighted quickunion --- %s seconds ---" % (time.time() - start_time),prg.N,max(prg.size),prg.comp)
plt.imshow(B)
plt.show()

start_time=time.time()
file1=open("largeUF.txt","r")
lines=file1.readlines()
N=int(lines.pop(0))
prg=UF_weightedQU_mod(N)
for line in lines:
    pq=line.split()
    prg.weightedQUmod1(int(pq[0]),int(pq[1]))
B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
print("weighted quickunion --- %s seconds ---" % (time.time() - start_time),prg.N,max(prg.size),prg.comp)
plt.imshow(B)
plt.show()
