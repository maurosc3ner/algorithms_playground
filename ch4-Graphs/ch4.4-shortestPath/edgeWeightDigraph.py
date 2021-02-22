# from my_file import myClass
from BagDE import BagDE
from directedEdge import directedEdge

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

# prg=edgeWeightDigraph(10)
        