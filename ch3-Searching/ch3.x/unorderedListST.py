# This is a client implementation to test symbol tables
import re # for regular expression
import time
class node:
    def __init__(self,key,value):
        super().__init__()
        self.key=key
        self.value=value
class listSQST:
    def __init__(self):
        super().__init__()
        self.arr=[]
    def isEmpty(self):
        return True if len(self.arr)==0 else False
    def size(self):
        return len(self.arr)
    def put(self,key,value):
        for nodei in self.arr:
            if(nodei.key==key):
                nodei.value=value
                return
        self.arr.insert(0,node(key,value))
    def contains(self,key):
        for node in self.arr:
            if(node.key==key):
                return True
        return False
    def keys(self):
        keys=[]
        for node in self.arr:
            keys.append(node.key)
        return keys
    def get(self, key):
        for node in self.arr:
            if(node.key==key):
                return node.value
        return None
    def print(self):
        chain=""
        for node in self.arr:
            # print(node.key,node.value)
            chain=chain+"K:"+str(node.key)+" V:"+str(node.value)+"; "
        return chain
    def delete(self,key):
        for i,node in enumerate(self.arr):
            # print(node,i.key)
            if(node.key==key):
                temp=node
                self.arr.pop(i)
                return temp

def findMax(arr):
    keys=arr.keys()
    maxNode=node("",0)
    for key in keys:
        curV=arr.get(key)
        if(curV>maxNode.value):
            maxNode.key=key
            maxNode.value=curV
    return maxNode

prg=listSQST()
print(prg.print(),prg.size(),prg.isEmpty())
file1=open("tinyTale.txt","r")
file1=open("Tale.txt","r")
# file1=open("leipzig1M.txt","r")
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
                if not prg.contains(w):
                    prg.put(w,1)
                else:
                    prg.put(w,prg.get(w)+1)
print("unordered sequential search --- %s seconds ---" % (time.time() - start_time))
tempN=findMax(prg)



print(prg.size())
print("Max:",tempN.key,":",tempN.value)

# tale 4.7s
# leipzig1M 
