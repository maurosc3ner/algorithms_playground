

class ex_1_1_27:
    def binomial(self,size,k,p):
        print(size,k,p,1-p)
        if (size==0 and k==0): return 1.0
        if (size<0 or k<0): return 0.0

        return ((1.0-p)*self.binomial(size-1,k,p)+p*self.binomial(size-1,k-1,p))

    def main(self):
        print(self.binomial(100,50,0.25))
        # print(self.binomial(5,2,0.25))

programa=ex_1_1_27()
programa.main()