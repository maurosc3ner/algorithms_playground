
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

prg=listSQST()
print(prg.print(),prg.size(),prg.isEmpty())
prg.put("s",0)
prg.put("e",1)
prg.put("a",2)

print(prg.print(),prg.size(),prg.isEmpty(),prg.contains("W"),prg.keys(),prg.get("W"))
prg.delete("a")
print(prg.print(),prg.size(),prg.isEmpty(),prg.contains("e"),prg.keys(),prg.get("e"))