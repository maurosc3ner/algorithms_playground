

class Node:
    def __init__(self,key,value,N):
        super().__init__()
        self.left=None
        self.right=None
        self.key=key
        self.value=value
        self.nChildren=N

class bst:
    def __init__(self):
        super().__init__()
        self.root=None
    def size(self):
        return self._size(self.root)
    # en python no hay method overloading nativo, toca mediante dispatcher
    def _size(self,root):
        if(root==None): return 0
        else: return root.nChildren

    def maxH(self):
        return self._maxH(self.root)
    
    def _maxH(self,x):
        if(x==None): return -1
        l=self._maxH(x.left)
        r=self._maxH(x.right)
        if(l>r): return l+1
        else: return r+1

    def get(self,key):
        return self._get(self.root,key)

    def _get(self,node,key):
        if(node==None): return None
        if(key<node.key): return self._get(node.left,key)
        elif(key>node.key): return self._get(node.right,key)
        else: return node.value
    
    def put(self,key,value):
        self.root=self._put(self.root,key,value)

    def _put(self,nod,key,value):
        if(nod==None): return Node(key,value,1)
        if(key<nod.key): nod.left=self._put(nod.left,key,value)
        elif(key>nod.key): nod.right=self._put(nod.right,key,value)
        else: # es porque ya existe entonces debemos actualizarlo
            nod.value=value
            # aqui se puede optimizar returnando de una pq no se 
            # crearon nuevos hijos no hay que sumar
            return nod
        nod.nChildren=self._size(nod.left)+self._size(nod.right)+1
        return nod
    
    def min(self):
        temp=self.root
        while(temp.left):
            temp=temp.left
        return temp
    def _min(self,x):
        temp=x
        while(temp.left):
            temp=temp.left
        return temp

    def max(self):
        temp=self.root
        while(temp.right):
            temp=temp.right
        return temp

    def floor(self,key):
        x=self._floor(self.root,key)
        return x

    def _floor(self,node,key):
        if(node==None): return None
        if(node.key==key): return node
        if(key<node.key): return self._floor(node.left,key)
        t=self._floor(node.right,key)
        if (t): return t
        else: return node
        
    def ceil(self,key):
        x=self._ceil(self.root,key)
        return x
    
    def _ceil(self,node,key):
        if(node==None): return None
        if(key==node.key): return node
        if(key>node.key): return self._ceil(node.right,key)
        t=self._ceil(node.left,key)
        if (t): return t
        else: return node
    
    def rank(self,key):
        return self._rank(self.root,key)
    
    def _rank(self,x,key):
    # el numero de nodos menores que la key
        if(x==None): return 0
        if (key<x.key): return self._rank(x.left,key)
        elif(key>x.key): return 1+self._size(x.left)+self._rank(x.right,key)
        else: return self._size(x.left)

    def select(self,idx):
        return self._select(self.root,idx)
    
    def _select(self,x,idx):
        # como es el inverso del rank, retornamos es el nodo
        if x==None: return None
        t=self._size(x.left)
        if t>idx: return self._select(x.left,idx)
        # como me paso para la derecha, le resto a idx el tamanho de la izquiera y el padre
        elif t<idx: return self._select(x.right,idx-t-1) 
        else: return x

    def deleteMin(self):
        #borra el nodo mas pequenho (a la izquierda) si tiene hijo a la derecha lo usa como su reemplazo
        root = self._deleteMin(self.root)

    def _deleteMin(self,x):
        #condicion de parada el hijo mas izquierdo
        if(x.left==None): return x.right
        x.left=self._deleteMin(x.left)
        x.nChildren=self._size(x.left)+self._size(x.right)+1
        return x

    def delete(self, key):
        """
        docstring
        """
        self.root=self._delete(self.root,key)

    def _delete(self, x,key):
        """
        docstring
        """
        if(x==None): return None
        if(key<x.key): x.left=self._delete(x.left,key)
        elif(key>x.key): x.right=self._delete(x.right,key)
        else:
            if(x.right==None): return x.left
            if(x.left==None): return x.right
            t=x
            x=self._min(t.right)
            x.right=self._deleteMin(t.right)
            x.left=t.left
        x.nChildren=self._size(x.left)+self._size(x.right)+1
        return x

    def inorder(self):
        keys=[]
        self._inorder(self.root,keys)
        print(keys)

    def _inorder(self,node,keys):
        if(node==None): return keys
        self._inorder(node.left,keys)
        print("k:",node.key," v:",node.value," ch:",node.nChildren)
        keys.append(node.key)
        self._inorder(node.right,keys)
    
    def preorder(self):
        keys=[]
        self._preorder(self.root,keys)
        print(keys)

    def _preorder(self,node,keys):
        
        if(node==None): return keys
        keys.append(node.key)
        self._preorder(node.left,keys)
        self._preorder(node.right,keys)
        # print("k:",node.key," v:",node.value," ch:",node.nChildren)
        

    def posorder(self):
        keys=[]
        self._posorder(self.root,keys)
        print(keys)

    def _posorder(self,node,keys):
        if(node==None): return keys
        self._posorder(node.left,keys)
        self._posorder(node.right,keys)
        # print("k:",node.key," v:",node.value," ch:",node.nChildren)
        keys.append(node.key)


prg=bst()
# prg.put(50,0)
# prg.put(30,0)
# prg.put(20,0)
# prg.put(40,0)
# prg.put(70,0)
# prg.put(60,0)
# prg.put(80,0)
# prg.inorder()
# print(prg.root.key)

# searchexm
# prg.put("s",0)
# prg.put("e",1)
# prg.put("a",2)
# prg.put("r",3)
# prg.put("c",4)
# prg.put("h",5)
# prg.put("e",6)
# prg.put("x",7)
# prg.put("m",7)
# prg.inorder()

# # prg.preorder()
# # prg.posorder()

# print(prg.root.key,prg.get("s"),prg.min().key,prg.max().key,prg.floor("g").key,prg.floor("r").key,prg.floor("a"), prg.maxH())
# print(prg.ceil("g").key,prg.ceil("r").key,prg.ceil("a").key,prg.ceil("z"),prg.select(3).key,prg.rank("h"))
# print(prg.deleteMin(),prg.delete("h"),prg.maxH())
prg.inorder()
# aceehrsx
# prg.put("a",0)
# prg.put("c",1)
# prg.put("e",2)
# prg.put("e",3)
# prg.put("h",4)
# prg.put("r",5)
# prg.put("s",6)
# prg.put("x",7)
# prg.inorder() # inorder lo reversa si es metido en orden
# prg.preorder() # preorder lo reversa si es metido en orden
# prg.posorder() # igual
# print(prg.root.key)

prg.put(5,0)
prg.put(3,1)
prg.put(7,2)
prg.put(2,3)
prg.put(6,4)
prg.put(8,5)
prg.put(9,6)
# prg.inorder()
# prg.preorder()
# prg.posorder()
print(prg.maxH())

# prg.put(45,0)
# prg.put(25,1)
# prg.put(75,2)
# prg.put(15,3)
# prg.put(35,4)
# prg.inorder()
# prg.preorder()
# prg.posorder()