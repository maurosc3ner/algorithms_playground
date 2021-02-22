import numpy as np

class ex_1_1_13:

    def main(self):
        Ori=np.array([[1,2,3],[4,5,6]])
        miTransp=np.empty([Ori.shape[1],Ori.shape[0]])
        print(Ori)
        # print(miTransp)
        for m in range(0,Ori.shape[0]):
            for n in range(0, Ori.shape[1]):
                miTransp[n,m]=Ori[m,n]
        print(miTransp)

programa=ex_1_1_13()
programa.main()