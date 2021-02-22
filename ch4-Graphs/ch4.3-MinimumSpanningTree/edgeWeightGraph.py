


class Edge:
    def __init__(self,v,w,weight):
        super().__init__()
        self.weight=weight
        self.v=v
        self.w=w
    
    def getWeight(self):
        return self.weight

    def either(self):
        return self.v

    def other(self, vertex):
        if (self.v==vertex): return self.w
        elif self.w==vertex: return self.v
        else : return None

    def toString(self):
        return str(self.v)+"-"+str(self.w)+" "+str(self.weight)

    def compareTo(self,that):
        if self.weight>that.getWeight(): return +1
        elif self.weight<that.getWeight(): return -1
        else: return 0

class Bag:
    def __init__(self):
        super().__init__()
        self.bag=list()

    def isEmpty(self):
        return len(self.bag)==0

    def size(self):
        return len(self.bag)

    def addItem(self,edge):
        self.bag.insert(0,edge)

    # iterador custom del objeto bag
    def __iter__(self):
        return iter(self.bag)

class edgeWeightGraph:
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

    def addEdge(self,edge):
        # como es un grafo pesado no direccionado debemos agregarlo en ambos vertices
        v=edge.either()
        w=edge.other(v)
        self.adj[v].addItem(edge)
        self.adj[w].addItem(edge)
        self.E+=1

    def toString(self):
        s=str(self.V) +" vertices, "+str(self.E)+" edges, weight\n"
        for i in range(0,self.V):
            for j in self.getAdj(i):
                s+=str(i)+": "
                # print(j.toString())
                s+=str(j.other(i))+" "+str(j.getWeight())
                s+="\n"
        return s

# file1=open("ch4.3-MinimumSpanningTree/tinyEWG.txt","r")
file1=open("ch4.3-MinimumSpanningTree/1000EWG.txt","r")
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

