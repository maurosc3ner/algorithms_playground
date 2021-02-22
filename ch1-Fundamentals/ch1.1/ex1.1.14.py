class ex_1_1_14:
    def manualMultip(self,x):
        acum=2
        idx=1
        # print(acum,idx,x)
        if x==0:
            return (1)
        else:
            while(idx<x):
                acum=acum*2
                idx=idx+1
                # print(acum,idx,x)
            return acum
    def manualLg(self,miN):
        x=-1
        res=0
        while(res<=miN):
            x+=1
            res=self.manualMultip(x)   
        x=x-1
        return x

    def main(self):
        N=int(input("Enter an integer >>>"))
        print(self.manualLg(N))
        # print(self.manualMultip(12))



programa=ex_1_1_14()
programa.main()