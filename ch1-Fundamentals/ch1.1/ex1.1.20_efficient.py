import numpy as np
import sys

class ex_1_1_20:
    def __init__(self,N):
        super().__init__()
        self._factArr=np.empty(N+1)
        self._factArr[0]=1
        self._N=N
        for j in range(1,self._N+1):
            self._factArr[j]=self._factArr[j-1]*j
    def main(self):
        print(self._factArr)
        print("N!=",self._factArr[self._N],", Ln(N!)=",np.log(self._factArr[self._N]))

n1=int(input('ln(N!):'))
programa=ex_1_1_20(n1)
programa.main()