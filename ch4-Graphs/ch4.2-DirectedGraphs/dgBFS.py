import numpy as np

class Bag:
    def __init__(self):
        super().__init__()
        self.bag=list()
    
    def addVertex(self,v):
        self.bag.insert(0,v)

    def __iter__(self):
        return iter(self.bag)

class DiGraph:
    def __init__(self,v,e):
        super().__init__()
        self.V=v
        self.E=e
        self.adj=list()
        for i in range(v):
            self.adj.append(Bag())
        
    def addEdge(self,v,w):
        self.adj[v].addVertex(w)

    def getV(self):
        return self.V
    
    def getAdj(self,v):
        return self.adj[v]

    def toString(self):
        s=str(self.V)+" vertices, "+str(self.E)+" edges.\n"
        for i in range(0,self.V):
            s+=str(i)+": "
            for j in self.getAdj(i):
                s+=str(j)+" "
            s+="\n"
        return s

class directedBFS:
    def __init__(self,graph,source):
        super().__init__()
        self.s=source
        self.marked=np.zeros(graph.getV(),dtype=bool)
        self.edgeTo=np.zeros(graph.getV(),dtype=int)
        self.distTo=np.zeros(graph.getV(),dtype=int)
        self.count=0
        self.bfs(graph,source)
        
    def bfs(self, g,v):
        """
        se expande de forma no recursiva con una queue
        """
        queue=list()
        queue.append(v)
        self.marked[v]=True
        self.distTo[v]=0
        self.count+=1
        while(len(queue)!=0):
            current=queue.pop(0)
            for i in g.getAdj(current):
                if not self.marked[i]:
                    self.edgeTo[i]=current
                    self.distTo[i]=self.distTo[current]+1
                    self.marked[i]=True
                    self.count+=1
                    queue.append(i)

    def hasPathTo(self,v):
        return self.marked[v]
    
    def pathTo(self,v):
        if self.marked[v]==0: return None
        path=list()
        i=v
        while i!=self.s:
            print(self.s,v,path,i)
            path.append(i)
            i=int(self.edgeTo[i])
        path.append(self.s)
        return path

    def getDist(self,v):
        return self.distTo[v]

file1=open("tinyDG.txt","r")
lines=file1.readlines()
v=int(lines.pop(0))
e=int(lines.pop(0))
prg=DiGraph(v,e)
print(len(lines), prg.V,prg.E)
for line in lines:
    # print(line.split())
    temp=line.split()
    prg.addEdge(int(temp[0]),int(temp[1]))

print(prg.toString())
myBFS=directedBFS(prg,9)
print(myBFS.hasPathTo(0),myBFS.pathTo(0),myBFS.getDist(0))

print(myBFS.hasPathTo(2),myBFS.pathTo(2),myBFS.getDist(2))