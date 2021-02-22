import numpy as np
import time
import matplotlib.pyplot as plt
import math
class UF_basic:
    def __init__(self,N):
        super().__init__()
        #array para los sitios
        self.id=np.arange(N)
        self.N=N
        self.acce=0
        #numero de componentes iniciales
        self.comp=N
        print("inicializado:",N)
    def find(self,i):
        self.acce+=1
        #este es el basico
        return self.id[i]

    def quickfind(self,p,q):
        pID=self.find(p)
        qID=self.find(q)
        #si ya estan el mismo componente lo desechamos
        if(pID==qID): return -1

        for item in range(0,self.N):
            if(pID==self.id[item]): 
                self.id[item]=qID
                self.acce+=1
        self.comp-=1

start_time=time.time()
file1=open("tinyUF_1.5.1.txt","r")
lineas1=file1.readlines()
N=lineas1.pop(0)
prg=UF_basic(int(N))

for linea in lineas1:
    pq=linea.split()
    print(pq)
    prg.quickfind(int(pq[0]),int(pq[1]))

# plt.imshow(prg.id)
print("Basic --- %s seconds ---" % (time.time() - start_time),prg.N,prg.acce,prg.comp,prg.id)
# plt.show()

start_time=time.time()
file1=open("mediumUF.txt","r")
lines=file1.readlines()
N=int(lines.pop(0))
prg=UF_basic(N)
for line in lines:
    pq=line.split()
    prg.quickfind(int(pq[0]),int(pq[1]))
B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
print("basic --- %s seconds ---" % (time.time() - start_time),prg.N,prg.acce,prg.comp)
plt.imshow(B)
plt.show()