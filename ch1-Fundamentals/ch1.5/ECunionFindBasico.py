import numpy as np
#importo libreria matplotlib
import matplotlib.pyplot as plt
import time
import math

class UF:
    def __init__(self,N):
        self.id=np.zeros([N,1])
        self.idC=np.zeros(N)
        self.N=N
        self.comp=N
        mi_n=0
        for i in range(0,N):
            self.id[i,0]=mi_n
            self.idC[i]=mi_n
            mi_n+=1
        print("inicializado:",N,mi_n)
    def find(self,i):
        if(i<=len(self.id)):
            return self.id[i,0]
    
    def union(self, p,q):
        pID=self.find(p)
        qID=self.find(q)
        # print("pq",pID,qID)
        if(pID==qID): return -1
        for i in range(0,len(self.id)):
            if(self.id[i,0]==pID): self.id[i,0]=qID
        self.comp-=1


start_time = time.time()
file1=open("tinyUF.txt","r")
lineas1=file1.readlines()
print(len(lineas1))
N=int(lineas1.pop(0))
prg=UF(N)

for linea1 in lineas1:
    pq=linea1.split()
    # print(pq,pq[0],pq[1])
    prg.union(int(pq[0]),int(pq[1]))
    # plt.imshow(np.transpose(prg.id))
    # plt.show()
plt.imshow(np.transpose(prg.id))
# print(prg.comp)
print("Basic --- %s seconds ---" % (time.time() - start_time),prg.N,prg.comp)
plt.show()
# start_time = time.time()
# file1=open("mediumUF.txt","r")
# lineas1=file1.readlines()
# print(len(lineas1))
# N=int(lineas1.pop(0))
# prg=UF(N)
# fig1, ax1 = plt.subplots()
# B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
# ax1=plt.imshow(B)
# i=0
# for linea1 in lineas1:
#     pq=linea1.split()
#     print(i)
#     prg.union(int(pq[0]),int(pq[1]))
#     i+=1
#     B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
#     ax1.set_data(B)
#     fig1.canvas.draw_idle()
#     plt.pause(0.01)

# print("Basic Medium file--- %s seconds ---" % (time.time() - start_time),prg.N,prg.comp)
# plt.show()

start_time = time.time()
file1=open("largeUF.txt","r")
lineas1=file1.readlines()
print(len(lineas1))
N=int(lineas1.pop(0))
prg=UF(N)
fig1, ax1 = plt.subplots()
B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
ax1=plt.imshow(B)
i=0
for linea1 in lineas1:
    pq=linea1.split()
    print(i)
    prg.union(int(pq[0]),int(pq[1]))
    i+=1
    # B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
    # ax1.set_data(B)
    # fig1.canvas.draw_idle()
    # plt.pause(0.01)
print(len(prg.id),prg.comp)
B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
ax1.set_data(B)
print("Basic largeUF--- %s seconds ---" % (time.time() - start_time))
plt.show()