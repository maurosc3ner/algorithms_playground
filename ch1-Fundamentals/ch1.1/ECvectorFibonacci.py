# al usar el arreglo permitimos reusar los calculos anteriores ya que guardamos sus resultados
# en el array. Esto hace que solo se haga un nuevo calculo que es la suma, en vez de las llamadas sucesivas recursivas

import numpy as np
class vectorFibonacci:

    def __init__(self):
        super().__init__()
        self._vect=np.zeros(90)
        self._vect[0]=0
        self._vect[1]=1
        for j in range (2,90):
            self._vect[j]=self._vect[j-1]+self._vect[j-2]  

    # def fibonator(self,N):
          
    
    def main(self):
        # print(self._vect)
        for i in range(0,90):
            print(i,">>>",self._vect[i])



programa=vectorFibonacci()
programa.main() 