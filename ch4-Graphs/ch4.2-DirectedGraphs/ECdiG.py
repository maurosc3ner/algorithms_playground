

class Bag:
    def __init__(self):
        super().__init__()
        self.bag=list()

    def size(self):
        return len(self.bag)
    
    def isEmpty(self):
        return len(self.bag)==0

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
    
    def getV(self):
        return self.V

    def getE(self):
        return self.E

    def addEdge(self,v,w):
        self.adj[v].addVertex(w)

    def getAdj(self,v):
        return self.adj[v]

    def toString(self):
        s=str(self.V)+" vertices, "+str(self.E)+" edges\n"
        for i in range(0,self.V):
            s+=str(i)+": "
            for j in self.getAdj(i):
                s+=str(j)+" "
            s+="\n"
        return s

# file1=open("tinyG.txt","r")
# file1=open("mediumG.txt","r")
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