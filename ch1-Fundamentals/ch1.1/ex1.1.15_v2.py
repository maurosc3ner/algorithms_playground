# Suponemos que el vector viene ordenado, sino se debe ordenar

import numpy as np

class ex_1_1_15:
    def histograma(self,arr,m):
        last=arr[0]
        hist=np.zeros(m,dtype=int)
        i=0
        idx=0
        # hist[1]=50
        print(arr.shape[0],hist)
        while(i<arr.shape[0]-1):
            hist[idx]=hist[idx]+1
            # si y solo el siguiente es diferente y esta ordenado
            # tenemos que pasar al siguiente bin
            # aumentamos el idx del histograma
            if(last!=arr[i+1]):
                # hist[idx]=hist[idx]+1
                idx+=1
                last=arr[i+1]
                print("if>",last,idx,i,hist)
            i=i+1
            
        hist[idx]+=1
        return(hist)


    def main(self):
        input=np.array([1,2,2,4,4,4])
        # input=np.array([3,3,3,4,7])
        m=4
        print(self.histograma(input,m))


programa=ex_1_1_15()
programa.main()