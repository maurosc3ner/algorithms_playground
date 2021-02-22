
import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt 
import sys
sys.setrecursionlimit(5000)

class Bag:
    def __init__(self):
        super().__init__()
        self.bag=list()

    def addItem(self,item):
        self.bag.insert(0,item)
    
    def isEmpty(self):
        return len(self.bag)==0
    
    def size(self):
        return len(self.bag)

    def __iter__(self):
        return iter(self.bag)

class Graph:
    def __init__(self,v,e):
        super().__init__()
        self.V=v
        self.E=e
        self.adj=list()
        for i in range(0,v):
            self.adj.append(Bag())
        self.visualG=nx.Graph()
    
    def getV(self):
        return self.V
    
    def getE(self):
        return self.E

    def addEdge(self,v,w):
        self.adj[v].addItem(w)
        self.adj[w].addItem(v)
        self.visualG.add_edge(v,w)

    def getAdj(self,v):
        return self.adj[v]



class BFS:
    def __init__(self,G,source):
        super().__init__()
        self.marked=np.zeros(G.getV())
        self.edgeTo=np.zeros(G.getV())
        self.distTo=np.full(G.getV(),10000000)
        
        self.color_map=["white" for x in range(G.getV())]
        self.s=source  
        self.count=0
        self.Bfs(G,source)
        plt.show()

    def Bfs(self,G,v):
        self.marked[v]+=1
        self.distTo[v]=0
        self.count+=1
        epoch=0
        Queue=list()
        Queue.append(v)
        while(len(Queue)!=0):
            cur=Queue.pop(0)
            # print(Queue)
            for w in G.getAdj(cur):
                epoch+=1

                if(self.marked[w]==0):
                    self.marked[w]+=1
                    self.count+=1
                    self.distTo[w]=self.distTo[cur]+1
                    self.edgeTo[w]=cur
                    Queue.append(w)
            self.visualize(G.visualG,epoch,cur)

    def getDist(self,v):
        return self.distTo[v]

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

    def visualize(self,G,epoch, current): 
        idx=0
        for node in G:
            # print(node,idx)
            if self.marked[node]==1:
                self.color_map[idx]='red'
            idx+=1

        # plt.clf()
        plt.title('Breed-First Search (red/blue=discovered/re-visited)\n Nodes discovered {}, current {}, iterations: {}, '.format(self.count,current,epoch))
        fig1.canvas.draw_idle()
        nx.draw_kamada_kawai(G,node_color=self.color_map,with_labels=True)
        plt.pause(0.000001)

file1=open("tinyG.txt","r")
# file1=open("mediumG.txt","r")
lines=file1.readlines()
v=int(lines.pop(0))
e=int(lines.pop(0))
prg=Graph(v+1,e+1) # custom edge para probar la distancia (kevin bacon number)
i=0
fig1, ax1 = plt.subplots(figsize=(18, 14))
for line in lines:
    temp=line.split()
    prg.addEdge(int(temp[0]),int(temp[1]))
    i+=1
prg.addEdge(3,13)
print(prg.visualG.nodes())

myBFS=BFS(prg,0)
print(myBFS.pathTo(9))
print(myBFS.pathTo(13),myBFS.getDist(13),myBFS.getDist(9))



