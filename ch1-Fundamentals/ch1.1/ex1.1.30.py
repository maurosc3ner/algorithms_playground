import numpy as np
import sys
class ex_1_1_30:
    def euclidesMCD(self,p,q,depth):
        depth+=1
        if(q==0):return p
        residuo=p%q
        # print(depth*" "+"p:"+str(p)+", q:"+str(q)+"r:"+str(residuo))
        return(self.euclidesMCD(q,residuo,depth))

    def main(self):
        print(self.euclidesMCD(105,24,0))
        print(self.euclidesMCD(7,11,0))

        dimr=int(sys.argv[1])
        dimc=int(sys.argv[2])
        # crea ya el arreglo lleno
        mimatriz=np.full([dimr,dimc],False,dtype=bool)
        print(mimatriz)

        for i in range(0,dimr):
            for j in range(0,dimc):
                gcd=self.euclidesMCD(i,j,0)
                print("gcd de ({},{}) es {}".format(i,j,gcd))
                if(gcd==1):
                    mimatriz[i,j]=True
                else: mimatriz[i,j]=False
        print(mimatriz)

programa=ex_1_1_30()
programa.main()