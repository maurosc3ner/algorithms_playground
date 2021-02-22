
class BagDE:
    def __init__(self):
        super().__init__()
        self.bag=list()

    def size(self):
        return len(self.bag)

    def isEmpty(self):
        return len(self.bag)==0

    def addItem(self,item):
        self.bag.insert(0,item)

    def __iter__(self):
        return iter(self.bag)