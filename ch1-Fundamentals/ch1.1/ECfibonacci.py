# 46 >>> 1836311903
# 47 >>> 2971215073
# 46 >>> 1836311903.0
# 47 >>> 2971215073.0
class fibonacci:
    
    def fibonator(self,N):
    # dos casos base
        if (N==0):
            return 0
        if(N==1):
            return 1
        
        return self.fibonator(N-2)+self.fibonator(N-1)

    def main(self):
        for i in range(0,90):
            print(i, ">>>",self.fibonator(i))
            


programa=fibonacci()
# print(programa.fibonator(9))

programa.main()