import numpy as np
class Edge:
    def __init__(self,v,w,weight):
        self.v=v
        self.w=w
        self.weight=weight

    def getWeight(self):
        return self.weight

    def either(self):
        return self.v

    def other(self,v):
        if self.v==v: return self.w
        elif self.w==v: return self.v
        else: None
    
    def compareTo(self,that):
        if self.weight>that.getWeight(): return +1
        elif self.weight<that.getWeight(): return -1
        else: return 0

    def toString(self):
        return str(self.v)+" "+str(self.w)+" "+str(self.weight)

class Bag:
    def __init__(self):
        super().__init__()
        self.bag=list()

    def size(self):
        return len(self.bag)

    def addItem(self,e):
        self.bag.insert(0,e)

    def __iter__(self):
        return iter(self.bag)

class UF:
    def __init__(self,N):
        self.id=np.zeros(N,dtype=int)
        self.N=N
        self.components=N
        for i in range(N):
            self.id[i]=i

    def find(self,p):
        return self.id[p]

    def connected(self,p,q):
        return self.id[p]==self.id[q]
    
    def union(self,p,q):
        pId=self.find(p)
        qId=self.find(q)
        if(pId==qId): 
            return
        for i in range(self.N):
            if(self.id[i]==pId): self.id[i]=qId
        self.components-=1

class priorityQueue:
    def __init__(self):
        super().__init__()
        self.pq=list()
    
    def isEmpty(self):
        return len(self.pq)==0

    def delMin(self):
        if len(self.pq)!=0:
            min=self.pq[0]
            minIdx=0
            for idx,item in enumerate(self.pq):
                if(item.getWeight()<min.getWeight()):
                    minIdx=idx
                    min=item
            return self.pq.pop(minIdx)
    
    def addItem(self,item):
        self.pq.append(item)

    def __iter__(self):
        return iter(self.pq)

class edgeWeightedGraph:
    def __init__(self,v):
        super().__init__()
        self.V=v
        self.E=0
        self.adj=list()
        for i in range(v):
            self.adj.append(Bag())

    def getV(self):
        return self.V

    def getE(self):
        return self.E

    def getAdj(self,v):
        return self.adj[v]    

    def addEdge(self,e):
        v=e.either()
        w=e.other(v)
        self.adj[v].addItem(e)
        self.adj[w].addItem(e)
        self.E+=1

    def getEdges(self):
        bagE=list()
        for v in range(self.V):
            for e in self.adj[v]:
                if (e.other(v)>v): 
                    bagE.append(e)
        return bagE    

    def toString(self):
        s=""
        s=str(self.V) +" vertices, "+str(self.E)+" edges, weight\n"
        for i in range(0,self.V):
            for j in self.getAdj(i):
                s+=str(i)+": "
                # print(j.toString())
                s+=str(j.other(i))+" "+str(j.getWeight())
                s+="\n"
        return s

class kruskal:
    def __init__(self,G):
        super().__init__()
        self.pq=priorityQueue()
        self.mstList=list()
        self.marked=np.zeros(G.getV())
        self.MST(G)

    def MST(self,G):
        uf=UF(G.getV())
        for e in G.getEdges():
            self.pq.addItem(e)

        while(not self.pq.isEmpty()):
            curEdge=self.pq.delMin()
            v=curEdge.either()
            w=curEdge.other(v)
            if (uf.connected(v,w)): continue
            uf.union(v,w)
            self.mstList.append(curEdge)

    def getMST(self):
        cost=0
        for e in self.mstList:
            cost+=e.getWeight()
        return self.mstList,cost

file1=open("ch4.3-MinimumSpanningTree/tinyEWG.txt","r")
# file1=open("ch4.3-MinimumSpanningTree/mediumEWG.txt","r")
lines=file1.readlines()
v=int(lines.pop(0))
e=int(lines.pop(0))
prg=edgeWeightedGraph(v)
print(len(lines), prg.V,prg.E)
for line in lines:
    # print(line.split())
    temp=line.split()
    newEdge=Edge(int(temp[0]),int(temp[1]),float(temp[2]))
    prg.addEdge(newEdge)

print(prg.toString())

mykrMST=kruskal(prg)
mst, cost=mykrMST.getMST()
print(cost)