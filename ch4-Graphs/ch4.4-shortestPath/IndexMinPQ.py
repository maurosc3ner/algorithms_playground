class IndexMinPQ:
    def __init__(self,numV):
        super().__init__()
        self.pq=list()
        self.keys=list()
        self.qp=list()
        for i in range(numV+1):
            self.keys.append(None)
            self.pq.append(None)
            self.qp.append(-1)
        self.n=0

    def isEmpty(self):
        return self.n==0

    def greater(self,i,j):
        return self.keys[self.pq[i]]>self.keys[self.pq[j]]

    def insert(self,idx,key):
        self.n+=1
        self.qp[idx]=self.n
        self.pq[self.n]=idx
        self.keys[idx]=key
        self.swim(self.n)

    def swap(self,i,j):
        swap=self.pq[i]
        self.pq[i]=self.pq[j]
        self.pq[j]=swap
        self.qp[self.pq[i]] = i
        self.qp[self.pq[j]] = j

    # se mantiene identico al minPQ
    def swim(self,k):
        while(k>1 and self.greater(k//2,k)):
            self.swap(k,k//2)
            k=k//2
    # se mantiene identico al minPQ
    def sink(self,k):
        while(2*k<=self.n):
            j=2*k
            if j<self.n and self.greater(j,j+1): j+=1
            if not self.greater(k,j): break
            self.swap(k,j)
            k=j
            
    def delMin(self):
        min=self.pq[1]
        minKey=self.keys[min]
        self.swap(1, self.n)
        self.n-=1
        self.sink(1)
        self.qp[min] = -1       # delete
        self.keys[min] = None 
        self.pq[self.n+1]=None
        return min

    def contains(self,i):
        return self.qp[i]!=-1

    def changeKey(self,i,key):
        self.keys[i] = key
        swim(self.qp[i])
        sink(self.qp[i])