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
        else: return None

    def compareTo(self,that):
        if self.weight>that.weight: return +1
        elif self.weight<that.weight: return -1
        else: return 0

    def toString(self):
        return str(self.v)+" "+str(self.w)+" "+str(self.weight)

class Bag:
    def __init__(self):
        self.bag=list()

    def addItem(self,edge):
        self.bag.insert(0,edge)
    
    def size(self):
        return len(self.bag)

    def isEmpty(self):
        return len(self.bag)==0

    def __iter__(self):
        return iter(self.bag)

class edgeWeightGraph:
    def __init__(self,v):
        self.V=v
        self.E=0
        self.adj=list()
        for i in range(v):
            self.adj.append(Bag())

    def addEdge(self,edge):
        v=edge.either()
        w=edge.other(v)
        self.adj[v].addItem(edge)
        self.adj[w].addItem(edge)
        self.E+=1
    
    def getV(self):
        return self.V
    
    def getE(self):
        return self.E

    def getAdj(self,v):
        return self.adj[v]

    # def edges(self):
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

class priorityQueue:
    def __init__(self):
        self.pq=list()

    def addItem(self,edge):
        self.pq.append(edge)

    def delMin(self):
        if len(self.pq)!=0:
            min=self.pq[0]
            minIdx=0
            for idx,i in enumerate(self.pq):
                if min.getWeight()>i.getWeight():
                    min=i
                    minIdx=idx
            return self.pq.pop(minIdx)

    def isEmpty(self):
        return len(self.pq)==0

    def __iter__(self):
        return iter(self.pq)

class lazyPrim:
    def __init__(self,G):
        self.pq=priorityQueue()
        self.mst=None
        self.marked=np.zeros(G.getV(),dtype=bool)
        self.weight=0
        # print(self.pq,self.marked,self.weight)
        self.MST(G)

    def MST(self,G):
        self.mst=list()
        # en Prim arrancamos en nodo cero
        self.visit(G,0)
        # print(self.marked,len(self.pq.pq))
        while(not self.pq.isEmpty()):
            currentEdge=self.pq.delMin()
            v=currentEdge.either()
            w=currentEdge.other(v)
            # print(currentEdge.toString(),v,w,len(self.pq.pq))
            # evitar los ineligibles
            if(self.marked[v] and self.marked[w]): continue
            self.mst.append(currentEdge)
            if(not self.marked[v]): self.visit(G,v)
            if(not self.marked[w]): self.visit(G,w)
    
    def getMST(self):
        cost=0
        for edge in self.mst:
            cost+=edge.getWeight()
        return self.mst,cost
    
    def visit(self,G,v):
        self.marked[v]=True
        for edge in G.getAdj(v):
            if not self.marked[edge.other(v)]:
                self.pq.addItem(edge)

# file1=open("ch4.3-MinimumSpanningTree/tinyEWG.txt","r")
file1=open("ch4.3-MinimumSpanningTree/mediumEWG.txt","r")
lines=file1.readlines()
v=int(lines.pop(0))
e=int(lines.pop(0))
prg=edgeWeightGraph(v)
print(len(lines), prg.V,prg.E)
for line in lines:
    # print(line.split())
    temp=line.split()
    newEdge=Edge(int(temp[0]),int(temp[1]),float(temp[2]))
    prg.addEdge(newEdge)

print(prg.toString())

myPrim=lazyPrim(prg)
mst, cost=myPrim.getMST()
print(cost)