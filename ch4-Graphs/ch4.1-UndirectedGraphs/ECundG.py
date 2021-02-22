# Se compone de dos clases, la primera necesita los vertices los edges y un bag
# la bolsa es una cola pero sin la posibilidad de remover y se inserta en cero
class bagLista:
    def __init__(self):
        super().__init__()
        self.bag=list()
    
    def agregarItem(self,item):
        self.bag.insert(0,item)

    def tamano(self):
        return len(self.bag)

    def vacia(self):
        return (self.tamano()==0)
    # iterador custom del objeto bag
    def __iter__(self):
        return iter(self.bag)
    
class Graph:
    def __init__(self,v,e):
        super().__init__()
        self.E=e
        self.V=v
        self.adj=list()
        for i in range(0,v):
            self.adj.append(bagLista())

    def E(self):
        return self.E

    def V(self):
        return self.V
    
    def addEdge(self,v,w):
        self.adj[v].agregarItem(w)
        self.adj[w].agregarItem(v)

    def getAdj(self,v):
        return self.adj[v]

    def toString(self):
        s=str(self.V) +" vertices, "+str(self.E)+" edges\n"
        for i in range(0,self.V):
            s+=str(i)+": "
            for j in self.getAdj(i):
                s+=str(j)+" "
            s+="\n"
        return s
            


# file1=open("tinyG.txt","r")
file1=open("mediumG.txt","r")
lines=file1.readlines()
v=int(lines.pop(0))
e=int(lines.pop(0))
prg=Graph(v,e)
print(len(lines), prg.V,prg.E)
for line in lines:
    # print(line.split())
    temp=line.split()
    prg.addEdge(int(temp[0]),int(temp[1]))

print(prg.toString())
# programa=bagLista()
# print(programa.tamano(), programa.vacia())
# for i in range(1,5):
#     programa.agregarItem(i)
# print(programa.tamano(), programa.vacia())
# promedio=0
# N=programa.tamano()
# for item in programa:
#     print(item)
#     promedio+=item
# print("media {}".format(promedio/N))