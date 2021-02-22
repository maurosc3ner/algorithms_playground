# template implementacion lista ordenada

class node:
    def __init__(self,key,value):
        super().__init__()
        self.key=key
        self.value=value

class binaryOrderedST:
    def __init__(self):
        super().__init__()
        self.arr=[]
    def size(self):
        return len(self.arr)
    def isEmpty(self):
        return True if self.size()==0 else False
    def min(self):
        return self.arr[0]
    def deleteMin(self):
        if(not self.isEmpty()): 
            self.arr.pop(0)
    def max(self):
        return self.arr[-1] # in python negative index start from the end
    def deleteMax(self):
        if(not self.isEmpty()): 
            self.arr.pop()  
    def select(self,idx): # devuelve la llave en la posicion idx
        if(idx>=0 and idx<self.size()):
            return self.arr[idx].key
    def rank(self,key): # asumiendo que esta ordenado, devuelve el numero de elementos menores a key
        # version no recursiva 
        lo=0
        hi=len(self.arr)-1
        while(lo<=hi):
            mid=lo+(hi-lo)//2
            if(self.arr[mid].key<key): lo=mid+1
            elif(self.arr[mid].key>key): hi=mid-1
            else: return mid
        return lo
    
    def get(self,key):
        if(not self.isEmpty()):
            idx=self.rank(key)
            if(idx<self.size() and self.arr[idx].key==key): return self.arr[idx].value
            else: return None

    def put(self,key,value):
        # se puede hacer a pedal moviendo todos los elementos a la derecha o con el metodo list.insert
        idx=self.rank(key)
        if(idx<self.size() and self.arr[idx].key==key): # significa que existe
            self.arr[idx].value=value
            return
        # aqui viene el for de mover si lo hicieramos a pata
        self.arr.insert(idx,node(key,value))
    def delete(self,key):
        idx=self.rank(key)
        if(idx<self.size() and self.arr[idx].key==key): 
            self.arr.pop(idx)
    def keys(self):
        keys=[]
        for obj in self.arr:
            keys.append(obj.key)
        return keys
    def print(self):
        chain=""
        for  obj in self.arr:
            chain=chain+"K:"+str(obj.key)+" V:"+str(obj.value)+"; "
        return chain
    def certification(self):
        if (not self.isEmpty()):
            if(0!=self.rank(self.select(0))): return False
            for i in range(1,self.size()):
                if(self.arr[i-1].key>self.arr[i].key): return False
                if(i!=self.rank(self.select(i))): return False
            return True
        return True
    def floor(self,key):
        idx=self.rank(key)
        if (idx<self.size() and self.arr[idx].key==key): return self.arr[idx]
        if(idx==0): return None
        else: return self.arr[idx-1] #no es cero y no esta en la lista entonces el mayor que sea menor a key
    def ceiling(self,key):
        idx=self.rank(key)
        if(idx==self.size()): return None
        else: return self.arr[idx]


prg=binaryOrderedST()
print(prg.print(),prg.size(),prg.isEmpty())
prg.put("s",0)
prg.put("e",1)
prg.put("a",2)
prg.put("r",3)
prg.put("c",4)
prg.put("h",5)
prg.put("e",6)
prg.put("x",7)
prg.put("a",8)
prg.put("m",9)
prg.put("p",10)
prg.put("l",11)
prg.put("e",12)
print(prg.print(),prg.floor("q").key,prg.ceiling("z"))
# print(prg.print(),prg.size(),prg.isEmpty(),prg.keys(),prg.get("a"))
# prg.delete("a")
# print(prg.print(),prg.size(),prg.isEmpty(),prg.keys(),prg.get("e"))
# prg.deleteMin()
# prg.deleteMax()
# print(prg.print(),prg.size(),prg.isEmpty(),prg.keys(),prg.get("e"))

# print(prg.certification())