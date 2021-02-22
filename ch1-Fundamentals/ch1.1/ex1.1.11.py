import numpy as np

class ex_1_1_11:
    def main(self):
        # creo el arreglo
        arr=np.array([[True,False,True],[False,True,True]])
        idx=-1
        idy=-1
        #Lo recorro
        for x in arr:
            idy+=1
            print("  ",end='')
            for j in range(0,3):
                idx+=1
                print(idx,end='')
            idx=-1
            print('\n'+str(idy)+'=',end='')
            for y in x:
                idy+1
                if y: print('*',end='')
                else: print('_',end='')
            print('\n')


programa=ex_1_1_11()
programa.main()