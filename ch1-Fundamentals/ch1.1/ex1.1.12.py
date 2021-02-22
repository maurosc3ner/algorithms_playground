import numpy as np

class ex_1_1_12:

    def main (self):
        arr=np.array([0,0,0,0,0,0,0,0,0,0])
        print(arr)
        
        for idx in range(0,10):
            arr[idx]=9-idx
        print(arr) # 9,8, ..., 1, 0
        for idx in range(0,10):
            arr[idx]=arr[arr[idx]]
        print(arr) # lo parte a la mitad y lo reversa
        
programa=ex_1_1_12()
programa.main()