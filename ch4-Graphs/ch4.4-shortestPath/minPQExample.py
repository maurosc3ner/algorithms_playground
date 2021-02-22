

class MinPQ:
    def __init__(self):
        super().__init__()
        self.minpq=list()
        self.minpq.append(None)
        self.n=0

    def swim(self,k): # promover hacia arriba
        while k>1 and self.minpq[k//2]>self.minpq[k]:
            self.swap(k//2,k)
            k=k//2

    def sink(self,k): #relegar -> hacia abajo
        while 2*k<=self.n:
            j=2*k
            if j<self.n and self.minpq[j]>self.minpq[j+1]: j+=1
            if not self.minpq[k]>self.minpq[j]: break
            self.swap(k,j)
            k=j

    def swap(self,p,q): #intercambiar posiciones del array
        swap=self.minpq[p]
        self.minpq[p]=self.minpq[q]
        self.minpq[q]=swap

    def insert(self,value):
        self.minpq.append(value)
        self.n+=1
        self.swim(self.n)

    def delMin(self):
        min=self.minpq[1]
        self.swap(1,self.n)
        self.n-=1
        self.minpq.pop()
        self.sink(1)
        return min
        

prg=MinPQ()

arr=["T","P","R","N","H","O","A","E","I","G"]
# arr.sort()
print(arr)

for i in arr:
    prg.insert(i)

print(prg.minpq)
print(prg.delMin(),prg.minpq)
print(prg.delMin(),prg.minpq)
print(prg.delMin(),prg.minpq)