# This is the client freq counter for the BST structure
import re # for regular expression
import time
class Node:
    def __init__(self,key,value,N):
        super().__init__()
        self.key=key
        self.value=value
        self.left=None
        self.right=None
        self.N=N

class bst:
    def __init__(self):
        super().__init__()
        self.root=None

    def size(self):
        return self._size(self.root)

    def _size(self,x):
        """
        docstring
        calcula el tamanho de cada nodo usando el campo adicional
        """
        if x==None: return 0
        return x.N
    
    def get(self,key):
        """
        docstring
        """
        return self._get(self.root,key)
    
    def _get(self,x,key):
        """
        docstring
        """
        if x==None: return None
        if(key<x.key): return self._get(x.left,key)
        elif(key>x.key): return self._get(x.right,key)
        else: return x.value
    
    def insert(self,key,value):
        """
        docstring
        """
        self.root=self._insert(self.root,key,value)

    def _insert(self, x,key,value):
        """
        inserta de forma recursiva, si es null crea nuevo nodo
        si es menor a la izq, si es mayor a la der, si es igual actualiza
        actualiza el tamaño, retorna la referencia
        """
        if x==None: return Node(key,value,1)
        if key<x.key: x.left=self._insert(x.left,key,value)
        elif key>x.key: x.right=self._insert(x.right,key,value)
        else: x.value=value 
        x.N=self._size(x.left)+self._size(x.right)+1
        return x

    def min(self):
        """
        docstring
        """
        return self._min(self.root)
    
    def _min(self, x):
        """
        docstring
        """
        if (x.left==None): return x
        return self._min(x.left)
    
    def max(self):
        """
        docstring
        """
        return self._max(self.root)
    
    def _max(self, x):
        """
        docstring
        """
        if (x.right==None): return x
        return self._max(x.right)
    
    def select(self, idx):
        """
        docstring
        """
        return self._select(self.root,idx).key

    def _select(self, x,idx):
        """
        docstring
        """
        if(x==None): return None
        t=self._size(x.left)
        if t>idx: return self._select(x.left,idx)
        elif t<idx: return self._self(x.right,idx-t-1)
        else: return x
    
    def rank(self, key):
        """
        docstring
        """
        return self._rank(self.root,key)

    def _rank(self,x,key):
        """
        Retorna el numero (int) de llaves menores a la llave buscada 
        de no encontrarla y ser la menor retorna 0
        """
        if x==None: return 0
        if key<x.key: return self._rank(x.left,key)
        elif key>x.key: return 1+ self._size(x.left)+self._rank(x.right,key)
        else: return self._size(x.left)

    def deleteMin(self):
        """
        siempre que vaya a insertar o borrar debe retornar la referencia a root
        """
        self.root=self._deleteMin(self.root)

    def _deleteMin(self, x):
        """
        docstring
        """
        if x.left==None: return x.right
        x.left=self._deleteMin(x.left)
        x.N=self._size(x.left)+self._size(x.right)+1
        return x

    def delete(self, key):
        """
        caso general Hibbard dilemma
        """
        self.root=self._delete(self.root,key)

    def _delete(self, x,key):
        """
        docstring
        """
        if(x==None): return None
        if key<x.key: x.left=self._delete(x.left,key)
        elif key>x.key: x.right=self._delete(x.right,key)
        else:
            if x.left==None: return x.right
            if x.right==None: return x.left
            # guardo referencia a borrar
            t=x
            # encuentro el candidato de reemplazo osea el minimo del arbol derecho
            # pero esto es arbitrario puede ser el maximo del arbol izquierdo
            x=self._min(t.right)
            # a ese minimo lo muevo, primero borrandolo del arbol derecho y retornando la referencia
            x.right=self._deleteMin(t.right)
            # y luego apuntando la izquierda guardada en t
            x.left=t.left
        x.N=self._size(x.left)+self._size(x.right)+1
        return x

    def inorder(self):
        """
        docstring
        """
        keys=[]
        self._inorder(self.root,keys)
        return keys
    
    def _inorder(self,x,keys):
        if(x==None): return keys
        self._inorder(x.left,keys)
        # print("k:",x.key," v:",x.value," ch:",x.N)
        keys.append(x.key)
        self._inorder(x.right,keys)

    def isEmpty(self):
        """
        docstring
        """
        return True if self.root==None else False

    def maxHeight(self):
        """
        docstring
        """
        return self._maxHeight(self.root)

    def _maxHeight(self, x):
        """
        docstring
        """
        if (x==None): return -1
        left=self._maxHeight(x.left)
        right=self._maxHeight(x.right)
        if left>right:
            return left+1
        else:
            return right +1
        
prg=bst()

# searchexm
# prg.insert("s",0)
# prg.insert("e",1)
# prg.insert("a",2)
# prg.insert("r",3)
# prg.insert("c",4)
# prg.insert("h",5)
# prg.insert("e",6)
# prg.insert("x",7)
# prg.insert("m",7)
# print(prg.inorder())
# print(prg.root.key,prg.get("s"),prg.min().key,prg.max().key)

def findMax(tree):
    keys=tree.inorder()
    maxNode=Node("",0,1)
    for key in keys:
        curV=tree.get(key)
        if(curV>maxNode.value):
            maxNode.key=key
            maxNode.value=curV
    return maxNode

prg=bst()
print(prg.size(),prg.isEmpty())
# file1=open("tinyTale.txt","r")
file1=open("Tale.txt","r")
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
                if vGetter==None:
                    prg.insert(w,1)
                else:
                    prg.insert(w,vGetter+1)

print("Binary Search Tree --- %s seconds ---" % (time.time() - start_time))
tempN=findMax(prg)
print(prg.size(),prg.maxHeight())
print("Max:",tempN.key,":",tempN.value)

#Tale.txt 0.2 seconds ---N=1828 h=24 Max: monseigneur : 104
#leipzig1M.txt 33s N=42244 h=36 Max: government : 31439