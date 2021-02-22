# implementacion con 
# lista enlazada no ordenada
import re # for regular expression
import time
class node:
    def __init__(self,key,value):
        super().__init__()
        self.key=key
        self.value=value
        self.next=None
class unorderedST:
    def __init__(self):
        super().__init__()
        self.first=None
        self.last=None
        self.N=0
    def size(self):
        return self.N
    def isEmpty(self):
        return True if self.N==0 else False
    def contains(self,k):
        temp=self.first
        while(temp):
            if(temp.key==k):
                return True
            temp=temp.next
        return False    
    def put(self,k,val):
        temp=self.first
        while (temp):
            if(temp.key==k): # ya existe solo actualizamos
                temp.value=val
                return  #encontrado debe parar el recorrido
            temp=temp.next
        newNode=node(k,val)
        self.N+=1
        if(self.first==None):
            self.first=newNode
            self.first.next=None
            self.last=self.first
        else:
            newNode.next=self.first
            self.first=newNode
    def delete(self,k):
        if(self.N>0):
            if(self.first==k):
                self.first=self.first.next
                if self.first==None: # quedo vacia
                    self.last=self.first
            else:
                temp=self.first
                while (temp.next):
                    if (temp.next.key==k):
                        temp.next=temp.next.next
                        if(temp.next==None): #era el ultimo nodo debo actualizar last
                            self.last=temp
                        self.N-=1
                        return
                    temp=temp.next
    def get(self,k):
        temp=self.first
        while(temp):
            if(temp.key==k):
                return temp.value
            temp=temp.next
        return None
    def keys(self):
        keys=[]
        temp=self.first
        while(temp):
            keys.append(temp.key)
            temp=temp.next
        return keys
    def print(self):
        temp=self.first
        chain=""
        while(temp):
            chain=chain+"K:"+str(temp.key)+" V:"+str(temp.value)+"; "
            temp=temp.next
        return chain

def findMax(arr):
    keys=arr.keys()
    maxNode=node("",0)
    for key in keys:
        curV=arr.get(key)
        if(curV>maxNode.value):
            maxNode.key=key
            maxNode.value=curV
    return maxNode

prg=unorderedST()
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

# tale 6.4s
# leipzig1M 
