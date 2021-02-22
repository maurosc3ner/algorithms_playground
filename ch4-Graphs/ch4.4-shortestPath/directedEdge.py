
class directedEdge:
    def __init__(self,v,w,weight):
        super().__init__()
        self.v=v
        self.w=w
        self.weight=weight

    def getFrom(self):
        return self.v
    
    def getTo(self):
        return self.w
        
    def getWeight(self):
        return self.weight
    
    def toString(self):
        return str(self.v)+" "+str(self.w)+" "+str(self.weight)