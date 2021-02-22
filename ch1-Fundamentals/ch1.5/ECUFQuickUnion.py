import numpy as np
import matplotlib.pyplot as plt
import time
import math

class UF_quickunion:
    def __init__(self,N):
        super().__init__()
        self.id=np.zeros([N,1])
        self.comp=N
        self.N=N
        for i in range(0,N):
            self.id[i,0]=i
        print("inicializado:",N,len(self.id))

    def find(self,i):
        #este ciclo lo que hace es llegar al root 
        # a traves de retornar el comoponente al que pertenece
        # print(i,self.id[i,0])
        while(i!=self.id[int(i),0]): 
            i=int(self.id[i,0])
        return i

    def quickunion(self,p,q):
        # a diferencia del basico, quick union se ahorra 
        # el ciclo de todo el array para cambiar los componentes
        # al solo tener que cambiar un elemento a el componente retornado padre1
        pID=self.find(p)
        qID=self.find(q)
        if(pID==qID): return -1
        self.id[pID,0]=qID
        self.comp-=1

file1=open("tinyUF.txt","r")
lineas1=file1.readlines()
# print(len(lineas1))
prg=UF_quickunion(int(lineas1.pop(0)))
# print(prg.id)
start_time = time.time()
for linea1 in lineas1:
    pq=linea1.split()
    # print(pq)
    prg.quickunion(int(pq[0]),int(pq[1]))
    # plt.imshow(np.transpose(prg.id))
    # plt.show()
print("QU tiny file--- %s seconds ---" % (time.time() - start_time),prg.N,prg.comp)



# start_time = time.time()
# file1=open("mediumUF.txt","r")
# lineas1=file1.readlines()
# # print(len(lineas1))
# N=int(lineas1.pop(0))
# prg=UF_quickunion(N)
# fig1, ax1 = plt.subplots()
# B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
# ax1=plt.imshow(B)
# i=0
# for linea1 in lineas1:
#     pq=linea1.split()
#     print(i)
#     i+=1
#     prg.quickunion(int(pq[0]),int(pq[1]))
#     B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
#     ax1.set_data(B)
#     fig1.canvas.draw_idle()
#     plt.pause(0.01)

# print("QU Medium file--- %s seconds ---" % (time.time() - start_time),prg.N,prg.comp)
# plt.show()

# start_time = time.time()
# file1=open("largeUF.txt","r")
# lineas1=file1.readlines()
# # print(len(lineas1))
# N=int(lineas1.pop(0))
# prg=UF_quickunion(N)
# # fig1, ax1 = plt.subplots()
# # B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
# # ax1=plt.imshow(B)
# for i in range(0,N):
#     print(i)
#     pq=lineas1.pop(0).split()
#     prg.quickunion(int(pq[0]),int(pq[1]))
#     # B=np.reshape(prg.id,(int(math.sqrt(N)),-1))
#     # ax1.set_data(B)
#     # fig1.canvas.draw_idle()
#     # plt.pause(0.01)
# # plt.show()
# print("QU large file--- %s seconds ---" % (time.time() - start_time),prg.N,prg.comp)
    