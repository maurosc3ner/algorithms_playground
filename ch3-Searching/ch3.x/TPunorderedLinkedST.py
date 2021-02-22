# esta version es una implementacion secuencial de 
# symbol table sin ordenar usando linked lists
# vamos a suponer que no hay keys repetidas
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

prg=unorderedST()
print(prg.print(),prg.size(),prg.isEmpty())
prg.put("s",0)
prg.put("e",1)
prg.put("a",2)

print(prg.print(),prg.size(),prg.isEmpty(),prg.contains("e"),prg.keys(),prg.get("e"))

prg.delete("s")
prg.delete("e")
prg.delete("a")
print(prg.print(),prg.size(),prg.isEmpty(),prg.contains("s"),prg.keys(),prg.get("s"))


            




