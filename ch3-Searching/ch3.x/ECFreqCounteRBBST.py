# red black implementation for balanced binary search trees
# it uses three balancing operations rotateLeft, rotateRigh, flipColors
# delete also requires an special implementatio to guarante logarithmic time

import re # for regular expression
import time

RED=True
BLACK=False

class Node: 
    def __init__(self,key,value,n,color=RED):
        super().__init__()
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        self.N=n
        self.color=color

class rb_bst:
    def __init__(self):
        super().__init__()
        self.root=None
    
    def size(self):
        return self._size(self.root)

    def _size(self,x):
        if x==None: return 0
        return x.N

    def get(self,key):
        return self._get(self.root,key)

    def _get(self,x,key):
        if x==None: return None
        if key<x.key: return self._get(x.left,key)
        elif key>x.key: return self._get(x.right,key)
        else: return x.value

    def inorder(self):
        keys=[]
        self._inorder(self.root,keys)
        return keys
    
    def _inorder(self,x,keys):
        if x==None: return
        self._inorder(x.left,keys)
        keys.append(x.key)
        self._inorder(x.right,keys)
    
    def isRed(self,x):
        if x==None: return False
        return x.color==RED

    def rotateLeft(self,h):
        x=h.right
        h.right=x.left
        x.left=h
        x.color=h.color
        h.color=RED
        x.N=h.N #hereda el tamanho de h
        h.N=self._size(h.left)+self._size(h.right)+1 # como cambio debo recalcular su tamanho
        return x

    def rotateRight(self,h):
        x=h.left
        h.left=x.right
        x.right=h
        x.color=h.color
        h.color=RED
        x.N=h.N #hereda el tamanho de h
        h.N= self._size(h.left)+self._size(h.right)+1 # como cambio debo recalcular su tamanho
        return x

    def flipColors(self,h):
        h.left.color=BLACK
        h.right.color=BLACK
        h.color=RED

    def insert(self,key,value):
        self.root=self._insert(self.root,key,value)
        self.root.color=BLACK

    def _insert(self,x,key,value):
        if(x==None): return Node(key,value,1,RED)
        if key<x.key: x.left=self._insert(x.left,key,value)
        elif key>x.key: x.right=self._insert(x.right,key,value)
        else: x.value=value
        # las tres nuevas reglas de rotacion
        if (self.isRed(x.right)) and (not self.isRed(x.left)): x=self.rotateLeft(x)
        if (self.isRed(x.left)) and (self.isRed(x.left.left)): x=self.rotateRight(x)
        if (self.isRed(x.left)) and (self.isRed(x.right)): self.flipColors(x)
        x.N=self._size(x.left)+self._size(x.right)+1
        return x
    
    def maxHeight(self):
        return self._maxHeight(self.root)
    
    def _maxHeight(self,x):
        if x==None: return -1
        left=self._maxHeight(x.left)
        right=self._maxHeight(x.right)
        if left>right:
            return left+1
        else: return right +1

    def isEmpty(self):
        return self.root==None

def findMax(tree):
    keys=tree.inorder()
    # print(keys)
    maxNode=Node("",0,1)
    for key in keys:
        curV=tree.get(key)
        if(curV>maxNode.value):
            maxNode.key=key
            maxNode.value=curV
    return maxNode

prg=rb_bst()
print(prg.size(),prg.isEmpty())
# file1=open("tinyTale.txt","r")
# file1=open("Tale.txt","r")
file1=open("leipzig1M.txt","r")
minLen=10

start_time=time.time()
lines=file1.readlines()
for line in lines:
    pq=re.findall(r"[\w']+", line)
    if(len(pq)>0):
        # print(pq)
        for word in pq:
            w=word.lower()
            if(len(w)>=minLen):
                vGetter=prg.get(w)
                # print("word:",w,"val:",vGetter)
                if vGetter==None:
                    prg.insert(w,1)
                else:
                    prg.insert(w,vGetter+1)

print("Red Black Binary Search Tree --- %s seconds ---" % (time.time() - start_time))
tempN=findMax(prg)
print(prg.size(),prg.maxHeight())
print("Max:",tempN.key,":",tempN.value)

#Tale.txt 0.2 seconds ---N=1828 h=14 Max: monseigneur : 104
#leipzig1M.txt 33s N=42244 h=21 Max: government : 31439