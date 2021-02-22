import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt 
import sys
sys.setrecursionlimit(5000)
class Bag:
    def __init__(self):
        super().__init__()
        self.bag=list()
    
    def add(self,item):
        self.bag.insert(0,item)
    
    def size(self):
        return len(self.bag)
    
    def isEmpty(self):
        return (len(self.bag)==0)
    
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
        # self.visualG=nx.OrderedGraph()
        self.pos = nx.circular_layout(self.visualG)
    
    def getV(self):
        return self.V

    def getE(self):
        return self.E

    def addEdge(self,v,w):
        # se agrega en los dos
        self.adj[v].add(w)
        self.adj[w].add(v)
        self.visualG.add_edge(v,w)
    
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

class Dfs:
    def __init__(self,G,s):
        super().__init__()
        # self.marked=np.zeros(G.getV(),dtype=bool)
        self.marked=np.zeros(G.getV())

        # creo la mascara para pintarlos y los relleno de blanco
        self.color_map= ["white" for x in range(G.getV())]
        self.edgeTo=np.zeros(G.getV())
        self.count=0
        self.s=s
        # print(self.marked,self.edgeTo,self.count,self.s,self.color_map)
        self.dfs(G,s,0)
        plt.show()

    def dfs(self,G,v,epoch):
        self.marked[v]+=1
        # print("node: ",v)
        # print(self.color_map)
        self.visualize(G.visualG,epoch,v)
        self.count+=1
        for w in G.getAdj(v):
            epoch+=1
            # if(not self.marked[w]):
            if(self.marked[w]==0):
                self.edgeTo[w]=v
                self.dfs(G,w,epoch)
            else: # si es visitado lo pinto de azul para demostrar la recursion
                self.marked[v]+=1
    
    def pathTo(self,v):
        if not self.marked[v]: return None
        path=list()
        i=v
        while i!=self.s:
            path.append(i)
            # print(self.edgeTo[i])
            i=int(self.edgeTo[i])
        path.append(self.s)
        return path
    
    def visualize(self,G,epoch, current): 
        idx=0
        for node in G:
            # print(node,idx)
            if self.marked[node]==1:
                # color_map.append('red')
                self.color_map[idx]='red'
            elif self.marked[node]>1: 
                # color_map.append('white') 
                self.color_map[idx]='blue'
            idx+=1

        # plt.clf()
        plt.title('Depth First Search (red/blue=discovered/re-visited)\n Nodes discovered {}, current {}, iterations: {}, '.format(self.count,epoch,current))
        fig1.canvas.draw_idle()
        nx.draw_kamada_kawai(G,node_color=self.color_map,with_labels=True)
        plt.pause(0.00001)

# file1=open("tinyG.txt","r")
file1=open("mediumG.txt","r")
lines=file1.readlines()
v=int(lines.pop(0))
e=int(lines.pop(0))
prg=Graph(v,e)
i=0
fig1, ax1 = plt.subplots(figsize=(18, 14))
for line in lines:
    temp=line.split()
    prg.addEdge(int(temp[0]),int(temp[1]))
    i+=1

print(prg.visualG.nodes())

myDFS=Dfs(prg,0)
# print(myDFS.pathTo(9))

