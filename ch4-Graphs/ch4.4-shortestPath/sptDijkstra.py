from BagDE import BagDE
from directedEdge import directedEdge
from edgeWeightDigraph import edgeWeightDigraph
from IndexMinPQ import IndexMinPQ

import numpy as np

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

file1=open("ch4.4-shortestPath/tinyEWD.txt","r")
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

