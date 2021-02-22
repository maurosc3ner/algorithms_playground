import math
import numpy as np
import time
import matplotlib.pyplot as plt

class weighted_UF:
    def __init__(self,N):
        super().__init__()
        self.id=np.arange(N)
        self.size=np.ones(N)
        self.N=N
        self.comp=N
        print("inicializado:",N,len(self.id))


    def find(self,i):
        while(i!=self.id[int(i)]):i=self.id[int(i)]
        return i
    
    def weighted_qunion(self,p,q):
        pID=self.find(p)
        qID=self.find(q)
        if(pID==qID): return -1
        # la idea es tomar el arbol mas pequeno para anexarlo al grande
        # y asi ir balanceando los arboles construidos
        if(self.size[pID]<self.size[qID]):
            self.id[pID]=qID
            self.size[qID]+=self.size[pID]
        else:
            self.id[qID]=pID
            self.size[pID]+=self.size[qID]
        self.comp-=1

# start_time = time.time()
# file1=open("tinyUF.txt","r")
# lineas1=file1.readlines()
# print(len(lineas1))
# N=int(lineas1.pop(0))
# prg=weighted_UF(N)
# for linea1 in lineas1:
#     pq=linea1.split()
#     # print(pq,pq[0],pq[1])
#     prg.weighted_qunion(int(pq[0]),int(pq[1]))
#     # plt.imshow(np.transpose(prg.id))
#     # plt.show()
# # plt.imshow(np.transpose(prg.id))
# # plt.show()
# # print(prg.comp)
# print("WeQU tinyUF --- %s seconds ---" % (time.time() - start_time),prg.N,prg.comp)

start_time = time.time()
file1=open("mediumUF.txt","r")
lineas1=file1.readlines()
print(len(lineas1))
N=int(lineas1.pop(0))
prg=weighted_UF(N)
fig1, ax1 = plt.subplots()
B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
ax1=plt.imshow(B)
for linea1 in lineas1:
    pq=linea1.split()
    prg.weighted_qunion(int(pq[0]),int(pq[1]))
    # plt.imshow(np.transpose(prg.id))
    # B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
    # ax1.set_data(B)
    # fig1.canvas.draw_idle()
    # plt.pause(0.01)
print(len(prg.id),prg.comp)
# plt.show()
print("WeQU mediumUF--- %s seconds ---" % (time.time() - start_time),prg.N,max(prg.size),prg.comp)


start_time = time.time()
file1=open("largeUF.txt","r")
lineas1=file1.readlines()
print(len(lineas1))
N=int(lineas1.pop(0))
prg=weighted_UF(N)
fig1, ax1 = plt.subplots()
B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
ax1=plt.imshow(B)
fig1.canvas.draw_idle()
i=0
for linea1 in lineas1:
    pq=linea1.split()
    prg.weighted_qunion(int(pq[0]),int(pq[1]))
    # B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
    # ax1.set_data(B)
    # fig1.canvas.draw_idle()
    # plt.pause(0.01)
    # i+=1
    # print(i)
print(len(prg.id),prg.comp)
B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
ax1.set_data(B)
plt.show()
print("WeQU largeUF--- %s seconds ---" % (time.time() - start_time),prg.N,max(prg.size),prg.comp)