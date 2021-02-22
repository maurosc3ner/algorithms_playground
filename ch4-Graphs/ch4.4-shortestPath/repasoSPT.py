import numpy as np

class directedEdge:
    def __init__(self,v,w,weight):
        super().__init__()
        self.v=v
        self.w=w
        self.weight=weight
    def getFrom(self):
        return self.v
    def getTo(self):
        return self.w
    def getWeight(self):
        return self.weight
    def toString(self):
        return str(self.v)+" "+str(self.w)+" "+str(self.weight)

class BagDE:
    def __init__(self):
        super().__init__()
        self.bag=list()
    def size(self):
        return len(self.bag)
    def isEmpty(self):
        return len(self.bag)==0
    def addItem(self,item):
        self.bag.insert(0,item)
    def __iter__(self):
        return iter(self.bag)

class IndexMinPQ:
    def __init__(self,numV):
        super().__init__()
        self.pq=list()
        self.keys=list()
        self.qp=list()
        for i in range(numV+1):
            self.keys.append(None)
            self.pq.append(None)
            self.qp.append(-1)
        self.n=0
    def isEmpty(self):
        return self.n==0
    def greater(self,i,j):
        return self.keys[self.pq[i]]>self.keys[self.pq[j]]
    def insert(self,idx,key):
        self.n+=1
        self.qp[idx]=self.n
        self.pq[self.n]=idx
        self.keys[idx]=key
        self.swim(self.n)
    def swap(self,i,j):
        swap=self.pq[i]
        self.pq[i]=self.pq[j]
        self.pq[j]=swap
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j
    # se mantiene identico al minPQ
    def swim(self,k):
        while(k>1 and self.greater(k//2,k)):
            self.swap(k,k//2)
            k=k//2
    # se mantiene identico al minPQ
    def sink(self,k):
        while(2*k<=self.n):
            j=2*k
            if j<self.n and self.greater(j,j+1): j+=1
            if not self.greater(k,j): break
            self.swap(k,j)
            k=j      
    def delMin(self):
        min=self.pq[1]
        minKey=self.keys[min]
        self.swap(1, self.n)
        self.n-=1
        self.sink(1)
        self.qp[min] = -1       # delete
        self.keys[min] = None 
        self.pq[self.n+1]=None
        return min
    def contains(self,i):
        return self.qp[i]!=-1
    def changeKey(self,i,key):
        self.keys[i] = key
        swim(self.qp[i])
        sink(self.qp[i])
############
class edgeWeightDigraph:
    def __init__(self,v):
        super().__init__()
        self.V=v
        self.E=0
        self.adj=list()
        for i in range(v):
            self.adj.append(BagDE())
    def getV(self):
        return self.V
    def getE(self):
        return self.E
    def getAdj(self,v):
        return self.adj[v]
    def addEdge(self,e):
        v=e.getFrom()
        self.adj[v].addItem(e)
        self.E+=1
    def getEdges(self):
        bagE=BagDE()
        for v in range(self.V):
            for e in self.adj[v]:
                bagE.addItem(e)
        return bagE
    def toString(self):
        for v in range(self.V):
            for e in self.adj[v]:
                print(e.toString())


class Dijkstra:
    def __init__(self,G, source):
        super().__init__()
        # distTo hace la funcion de marked, si no hay path la distancia es infinita
        self.distTo=np.zeros(G.getV(),dtype=float) 
        self.marked=np.zeros(G.getV(),dtype=bool)
        self.edgeTo=list()
        self.pq=None
        self.s=source
        for i in range(G.getV()):
            self.edgeTo.append(None)
        
        print(source,self.distTo.tolist(),G.getV())
        self.SPT(G,source)

    def getDistTo(self,v):
        return self.distTo[v]

    def hasPathTo(self,v):
        return self.distTo[v]<float('inf')
    
    def pathTo(self,v):
        if self.hasPathTo(v) and v!=self.s: 
            path=list()
            e=self.edgeTo[v]
            # print(e,self.edgeTo[v],self.hasPathTo(v))
            while e.getFrom()!=self.s:
                path.insert(0,e)
                e=self.edgeTo[e.getFrom()]
            # e=self.edgeTo[e.getFrom()]
            path.insert(0,e)
            return path
        return []
        
    def SPT(self,G,s):
        #inicializo la fuente en 0.0 y los demas en distancia infinita
        self.distTo.fill(float('inf'))

        self.distTo[s]=0.0
        # inicializo la priority queue
        self.pq=IndexMinPQ(G.getV())
        self.pq.insert(s,0.0)
        print(s,self.distTo.tolist(),G.getV(),self.pq.qp,self.pq.keys)
        while(not self.pq.isEmpty()):
            self.relax(G,self.pq.delMin())

    # metodo base de dijkstra
    def relax(self,G,v):
        for edge in G.getAdj(v):
            w=edge.getTo()
            if self.distTo[w]>self.distTo[v]+edge.getWeight():
                self.distTo[w]=self.distTo[v]+edge.getWeight()
                self.edgeTo[w]=edge
                if(self.pq.contains(w)): 
                    self.pq.changekey(w,self.distTo[w])
                else:
                    self.pq.insert(w,self.distTo[w])

file1=open("tinyEWD.txt","r")
lines=file1.readlines()
v=int(lines.pop(0))
e=int(lines.pop(0))
prg=edgeWeightDigraph(v)
print(len(lines), prg.V,prg.E)

for line in lines:
    # print(line.split())
    temp=line.split()
    newEdge=directedEdge(int(temp[0]),int(temp[1]),float(temp[2]))
    prg.addEdge(newEdge)

print(prg.toString())
mySPT=Dijkstra(prg,0)

for e in range(prg.getV()):
    print(str(e)+" (w:"+str(mySPT.getDistTo(e))+")")
    for j in mySPT.pathTo(e):
        # for k in j:
        print(j.toString())
